import pycolmap as pc
from pathlib import Path
import sys
from IPython.display import clear_output

sys.path.append('/src/app')
sys.path.append('/src/')
sys.path.append('src')
from place_utils import localize_places

feature_conf = "superpoint_aachen"
matcher_conf = "superglue"

import numpy as np
import cv2
import tqdm
import os
# from IPython.display import clear_output

# Clear the output of the current cell
# clear_output()

def get_qt_vector(recon):
    res = {}
    for k,image in recon.images.items():
        qtvec = np.concatenate((image.qvec,image.tvec), axis=0)
        res[image.name] = qtvec
    return res

def matcher_localize(image_paths, dataset_name, weightNo, intrinsic,num=20, rank=5, cvtColor=None, limit=99999999):
    poses = {}
    count = 0
    for image_path in tqdm.tqdm(image_paths):
        # if "sr1-101_1561_16_1.jpg" not in image_path: continue
        args = {"name": dataset_name,
                "input": image_path,
                "num": num,
                "rank": rank,
                "feature_conf":feature_conf,
                "weight":weightNo,
                "matcher_conf":matcher_conf,}
        args['intrinsic'] = intrinsic
        print(args)
        image = cv2.imread(image_path)
        if cvtColor: image = cv2.cvtColor(image, cvtColor)
        queries = [(os.path.basename(image_path), image)]
        try:
            pose, rets, logs = localize_places(queries, args)
        except Exception as e:
            print(e)
            pose = "ERROR"
            # raise e
        poses[image_path] = pose
        count+=1
        if count == limit: break
        clear_output()
    return poses

def set_query_poses_to_model(recon, poses):
    """
    use output from matcher localize
    """
    for i, image in recon.images.items():
        image_name = image.name
        q = poses[image_name][0]['orientation']
        t = poses[image_name][0]['position']
        old_qvec = recon.images[i].qvec
        old_tvec = recon.images[i].tvec
        recon.images[i].tvec = np.array([t['x'], t['y'], t['z']])
        recon.images[i].qvec = np.array([q['w'], q['x'], q['y'], q['z']])
    print("set new camera poses success!")

from pathlib import Path
import os

def run_eval_pipeline(map_name, image_path, intrinsic, weightNo):
    txt=''
    map_path = Path("/src/matcher_engine/HierarchicalLocalization/PMUC_Dataset/") / map_name
    image_paths = [im.path for im in os.scandir(image_path)]
    poses = matcher_localize(image_paths, map_name, weightNo, intrinsic,limit=9999999)
    for k,v in poses.items():
        name = '/'.join(k.split("/")[-1:])
        if v == "ERROR":
            txt += f"{name},ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR\n"
        else:
            q = v[0]['orientation']
            t = v[0]['position']
            txt += f"{name},{t['x']},{t['y']},{t['z']},{q['w']},{q['x']},{q['y']},{q['z']}\n"
            # print(poses)
            # print([os.path.basename(i) for i in image_paths])
    return txt

from pathlib import Path
image_path = "/src/matcher_engine/HierarchicalLocalization/PMUC_Dataset/pavilion-20230314-narrow/db"
# image_path = '/src/matcher_engine/HierarchicalLocalization/PMUC_Dataset/bld4f1-20221101/db'
map_name = "pavilion-20230314-wide"
weightNo = 0
intrinsic = "/src/matcher_engine/HierarchicalLocalization/PMUC_Dataset/pavilion-20230314-narrow/narrow_estimated_intrinsic.txt"
txt = run_eval_pipeline(map_name, image_path, intrinsic, weightNo)
with open(Path(image_path) / "localize_result.txt", 'w') as f:
    f.write(txt)