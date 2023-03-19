import cv2
from pathlib import Path
import os

dataset_name = 'boat_condo'
video_name = 'VID_20230105_004303.mp4'
frame_skip = 10
def process(img):
    img = img[::-1,:,:]
    img = img[:,::-1,:]

    return img

dataset_path = Path("/src/matcher_engine/HierarchicalLocalization/datasets")
db_image_path = dataset_path / dataset_name / "images" / "db"

if not os.path.exists(str(db_image_path)):
    os.makedirs(db_image_path, exist_ok=False)

video = cv2.VideoCapture(str(dataset_path / dataset_name / video_name))


frame_number = 0

success, frame = video.read()

while success:
    cv2.imwrite(str(db_image_path / "frame{}.jpg".format(frame_number)), process(frame))

    video.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

    success, frame = video.read()

    frame_number += frame_skip

video.release()