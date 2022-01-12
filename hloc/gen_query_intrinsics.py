import os
from pathlib import Path
import pycolmap

def main(img_path, db_intrinsics_file, output_path, output_name, query_prefix=None):
    print('creating list of queries with intrinsics')
    db_intrins_param = None
    try:
        with open(db_intrinsics_file) as intfile:
            db_intrins_param = intfile.readline().rstrip()
            intfile.close()
    except:
        print('database intrinsic param does not exist')

    with open(output_path / output_name, 'w') as f:
        for root, dirs, files in os.walk(img_path):
            rel_dir = Path(os.path.relpath(root, img_path))
            for filename in files:
                if query_prefix is not None:
                    if not str(rel_dir).startswith(query_prefix):
                        continue
                if db_intrins_param is not None:
                    intrins_param = db_intrins_param
                else:
                    camera = pycolmap.infer_camera_from_image(root + '/' + filename)
                    params = [camera.model_name, camera.width, camera.height] + camera.params_to_string().split(',')
                    intrins_param = ' '.join(map(str, params))
                f.write(str(rel_dir / filename) + ' ' + intrins_param + '\n')
        f.close()
        print('queries with intrinsics file has been saved in ' +
              str(output_path) + '/' + str(output_name) + "'.")
