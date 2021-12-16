import cv2
import logging
import numpy as np
from pathlib import Path

from .utils.read_write_model import (
        read_cameras_binary, read_images_binary, read_model, write_model,
        qvec2rotmat, read_images_text, read_cameras_text)
def create_list_with_intrinsics(model, out, list_file=None, ext='.bin',
                                      image_dir=None):
    print('Creating a list of db images with intrinsics from the colmap model...')
    if ext == '.bin':
        images = read_images_binary(model / 'images.bin')
        cameras = read_cameras_binary(model / 'cameras.bin')
    else:
        images = read_images_text(model / 'images.txt')
        cameras = read_cameras_text(model / 'cameras.txt')

    name2id = {image.name: i for i, image in images.items()}
    if list_file is None:
        names = list(name2id)
    else:
        with open(list_file, 'r') as f:
            names = f.read().rstrip().split('\n')
    data = []
    for name in names:
        image = images[name2id[name]]
        camera = cameras[image.camera_id]
        w, h, params = camera.width, camera.height, camera.params

        if image_dir is not None:
            # Check the original image size and rescale the camera intrinsics
            img = cv2.imread(str(image_dir / name))
            assert img is not None, image_dir / name
            h_orig, w_orig = img.shape[:2]
            assert camera.model == 'SIMPLE_RADIAL'
            sx = w_orig / w
            sy = h_orig / h
            assert sx == sy, (sx, sy)
            w, h = w_orig, h_orig
            params = params * np.array([sx, sx, sy, 1.])

        p = [camera.model, w, h] + params.tolist()
        data.append(' '.join(map(str, p)))
    with open(out, 'w') as f:
        f.write('\n'.join(data))
    logging.info('a file has been saved in ' + "'" + str(out) + "'.")

#create_list_with_intrinsics(model=Path('outputs/sfm5/SFMrecons/sfm_superpoint+superpoint/models/0'),out=Path('outputs/sfm5/SFMrecons/sfm_superpoint+superpoint/with_intrinsics_m0.txt'),image_dir=Path('datasets/STMultiViu/images/dbST'))
