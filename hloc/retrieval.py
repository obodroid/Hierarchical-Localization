import sys
import h5py
from pathlib import Path

openibl_path = Path(__file__).parent / '../third_party/d2net'
sys.path.append(str(openibl_path))

import torch
import logging
import numpy as np
from tqdm import tqdm
import pprint
from .utils.image_dataset import ImageDataset
from .utils.base_model import dynamic_load
from .utils.tools import map_tensor
import os
from . import extractors, logger

class Retriever(torch.nn.Module):
    def __init__(self):
        super(Retriever, self).__init__()
        self.model = torch.hub.load('yxgeee/OpenIBL', 'vgg16_netvlad', pretrained=True).eval()
        self.register_buffer("std", torch.Tensor([0.00392156862745098, 0.00392156862745098, 0.00392156862745098]).reshape(1, -1, 1, 1))
        self.register_buffer("mean", torch.Tensor([0.48501960784313836, 0.4579568627450961, 0.4076039215686255]).reshape(1, -1, 1, 1))

    def forward(self, data):
        img = data["image"]
        b, c, h, w = img.shape
        normed = (img - self.mean)/self.std
        des = self.model(normed)
        return {
            "global_descriptor": des
        }

confs = {
    "openibl": {
        "preprocessing": {
            "resize": (480, 640),
            'grayscale': False,
        }
    }
}

device = 'cuda' if torch.cuda.is_available() else 'cpu'
# model = Retriever().eval().to(device)
Model = dynamic_load(extractors, "netvlad")
model = Model({"name":"netvlad"}).eval().to(device)

@torch.no_grad()
def main(conf, image_dir, export_dir, output_name, as_half=False):
    logging.info('Extracting global descriptors with configuration:'
                 f'\n{pprint.pformat(conf)}')

    custom_weight = export_dir.parent.parent / "state_dict_360000.pt"
    # custom_weight = export_dir / "netvlad_weight2.pt"

    logging.info("Looking for", str(custom_weight))
    if os.path.exists(custom_weight):
        raise Exception("use are using custom weight of netvlad")
        model.load_state_dict(torch.load(str(custom_weight))["weight"])
        logging.info('use custom weight for netvlad...')
    else:
        logging.info('use default weight for netvlad...')
        # raise Exception("use are using default weight of netvlad")

    loader = ImageDataset(image_dir, conf['preprocessing'])
    loader = torch.utils.data.DataLoader(loader, num_workers=0)

    descriptor_path = Path(export_dir, output_name)
    descriptor_path.parent.mkdir(exist_ok=True, parents=True)
    descriptor_file = h5py.File(str(descriptor_path), 'a')

    logging.info(f'Start delete query descriptor: {descriptor_path}')
    for key in descriptor_file.keys():
        if not key.startswith('db'):
            del descriptor_file[key]

    for data in tqdm(loader):
        if data['name'][0] in descriptor_file:
            continue

        pred = model(map_tensor(data, lambda x: x.to(device)))
        
        pred = {k: v[0].cpu().numpy() for k, v in pred.items()}

        if as_half:
            for k in pred:
                dt = pred[k].dtype
                if (dt == np.float32) and (dt != np.float16):
                    pred[k] = pred[k].astype(np.float16)

        grp = descriptor_file.create_group(data['name'][0])
        for k, v in pred.items():
            grp.create_dataset(k, data=v)

        del pred

    descriptor_file.close()
    logging.info('Finished exporting descriptors.')

    return descriptor_path

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--image_dir', type=Path, required=True)
    parser.add_argument('--export_dir', type=Path, required=True)
    parser.add_argument('--conf', type=str, default='openibl',
                        choices=list(confs.keys()))
    parser.add_argument('--output_name', type=Path, required=True)
    parser.add_argument('--as_half', action='store_true')
    args = parser.parse_args()
    main(confs[args.conf], args.image_dir, args.export_dir, args.output_name, args.as_half)
