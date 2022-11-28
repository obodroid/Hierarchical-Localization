from pathlib import Path
import os
registering_image = Path('/home/bob/Hierarchical-Localization/datasets/cubld4/db/')
image_list = os.listdir(registering_image)
with open('/home/bob/Hierarchical-Localization/cubld4_image_list.txt', 'w') as txt:
    for i in image_list:
        line = 'db/' + i
        txt.write(line)
        txt.write('\n')