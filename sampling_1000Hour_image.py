import os
import random 
import shutil
image_list = [i for i in os.scandir('/src/matcher_engine/HierarchicalLocalization/PMUC_Dataset/1000Hour_raw')]
img_idxs = list(range(len(image_list)))
random.shuffle(img_idxs)
print(img_idxs)
img_idxs = img_idxs
for i in img_idxs:
    im  = image_list[i]
    im_path = im.path
    place = im.name.split("_")[2]
    run_id = im.name.split("_")[1]
    if place != "16": continue
    print(im_path)
    shutil.copy(im_path, "/src/matcher_engine/HierarchicalLocalization/PMUC_Dataset/1000Hour_placeno16")