import pycolmap as pc
from pathlib import Path
import sys
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

def matcher_localize(image_paths, dataset_name, weightNo, num=20, rank=5, cvtColor=None, limit=99999999):
    poses = {}
    count = 0
    for image_path in tqdm.tqdm(image_paths):
        args = {"name": dataset_name,
                "input": image_path,
                "num": num,
                "rank": rank,
                "feature_conf":feature_conf,
                "weight":weightNo,
                "matcher_conf":matcher_conf,}
        print(args)
        image = cv2.imread(image_path)
        if cvtColor: image = cv2.cvtColor(image, cvtColor)
        queries = [(os.path.basename(image_path), image)]
        try:
            pose, rets, logs  = localize_places(queries, args)
            print("POSE",pose)
        except Exception as e:
            pose = "ERROR"
            print(e)
        poses[image_path] = pose
        count+=1
        if count == limit: break
        # clear_output()
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

def run_eval_pipeline(map_name, weightNo):
    txt=''
    map_path = Path("/src/matcher_engine/HierarchicalLocalization/PMUC_Dataset/") / map_name
    for i in os.scandir(map_path):
        print(i.name)
        if "db" == i.name or "qr" == i.name:
            image_paths = [im.path for im in os.scandir(i)]
            poses = matcher_localize(image_paths, map_name, weightNo, limit=9999999)
            for k,v in poses.items():
                name = '/'.join(k.split("/")[-2:])
                if v == "ERROR":
                    txt += f"{name},ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR\n"
                else:
                    q = v[0]['orientation']
                    t = v[0]['position']
                    txt += f"{name},{t['x']},{t['y']},{t['z']},{q['w']},{q['x']},{q['y']},{q['z']}\n"
            # print(poses)
            # print([os.path.basename(i) for i in image_paths])
    return txt

tasks = ["canteen-20221115", "cuparking-20221101", "dragon-20221115", "isl2-20221101", "essence-20221103", 'football-20221106', 'bld3f1-20221106', 'political-20221114', 'shellhut-20221109','bld4f1-upper-p06top19']
# weights = [[2],[2],[2],[2],[2]]
# tasks = ["isl2-20221101", "essence-20221103"]
# weights = [[2],[2]]
# tasks = ["football-20221106", "bld3f1-20221106"]
# weights = [[2],[2],[2],[2],[2],[2],[2]]
weight = 0
for task in tasks:
    map = task
    w = weight
    save_file = Path(f"/src/matcher_engine/HierarchicalLocalization/PMUC_outputs/{map}/weight{w}") / "localize_dbqr0"
    if os.path.exists(save_file): print("skipping", map); continue
    txt = run_eval_pipeline(map, w)
    open(save_file, "w").write(txt)