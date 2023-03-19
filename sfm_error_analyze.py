import pycolmap as pc
from pathlib import Path
import sys
import cv2

sys.path.append('/src/app')
sys.path.append('/src/')
sys.path.append('src')
from place_utils import localize_places

num = 20
pose_limit = 999999
dset = 'canteen-20221115'
output = 'canteen-20221115'
feature_conf = "superpoint_aachen"
matcher_conf = "superglue"
ransac_config_ref = "Default"
cvtColor = None
covis_clustering = True
datasetz_path = Path(f'/src/matcher_engine/HierarchicalLocalization/outputs/{output}')
variation = f"nt_nip_retr{num}"
if cvtColor is not None:
    variation += f"_cvtClr"
if covis_clustering:
    variation += f"_covis"
variation += "_FIXBUG_FixIntrs"
if ransac_config_ref:
    variation += f"_ransac{ransac_config_ref}"

sfm = datasetz_path / 'sfm_superpoint+superglue'

recon = pc.Reconstruction()

import numpy as np
import tqdm
import os
from IPython.display import clear_output


def get_qt_vector(recon):
    res = {}
    for k,image in recon.images.items():
        qtvec = np.concatenate((image.qvec,image.tvec), axis=0)
        res[image.name] = qtvec
    return res

def matcher_localize(image_paths, image_folder_path, dataset_name, num=20, rank=5, cvtColor=None, limit=9999):
    poses = {}
    count = 0
    for image_path in tqdm.tqdm(image_paths):
        full_image_path = os.path.join(image_folder_path, image_path)
        args = {"name": dataset_name,
                "input": full_image_path,
                "num": num,
                "rank": rank,
                "feature_conf":feature_conf,
                "matcher_conf":matcher_conf,}
        image = cv2.imread(full_image_path)
        if cvtColor: image = cv2.cvtColor(image, cvtColor)
        queries = [(os.path.basename(full_image_path), image)]
        pose = localize_places(queries, args)
        poses[image_path] = pose
        count+=1
        if count == limit: break
        clear_output()
    return poses

def set_query_poses_to_model(recon, poses):
    """
    use output from matcher localize
    """
    print("Assigning...")
    for i, image in recon.images.items():
        try:
            image_name = image.name
            q = poses[image_name][0]['orientation']
            t = poses[image_name][0]['position']
            old_qvec = recon.images[i].qvec
            old_tvec = recon.images[i].tvec
            recon.images[i].tvec = np.array([t['x'], t['y'], t['z']])
            recon.images[i].qvec = np.array([q['w'], q['x'], q['y'], q['z']])
            print(image_name, end=" ")
        except KeyError:
            pass
    print("set new camera poses success!")

recon.read(str((sfm)))
print(recon.summary())

qtvecs = get_qt_vector(recon)

os.chdir('/src')

image_paths = list(qtvecs.keys())
dataset_name = dset
image_folder_paths = f'/src/matcher_engine/HierarchicalLocalization/datasets/{dset}/images'
query_poses = matcher_localize(image_paths, image_folder_paths, dataset_name, cvtColor=cvtColor, num=num, limit=pose_limit)

import pickle 

#nt no translation in get pose ของพีมั่ม
#nip no inverse pose เหมือน get_pose จะ return แต่ inverse pose เลยลบ inverse pose ทิ้ง 
with open("/src/matcher_engine/HierarchicalLocalization/error_analyze/query_poses_"+dataset_name+f"_{variation}.pkl", "wb") as f:
    pickle.dump(query_poses, f)

set_query_poses_to_model(recon, query_poses)

os.chdir('/src/matcher_engine/HierarchicalLocalization/error_analyze')

os.makedirs(output+f"_{variation}", exist_ok=False)
recon.write(output+f"_{variation}")