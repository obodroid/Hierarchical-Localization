import os
from pathlib import Path


def query_intrinsics(img_path, db_intrinsics_file, output_path, output_name):
    print('creating list of queries with intrinsics...')
    with open(db_intrinsics_file) as intfile:
        intrins_param = intfile.readline().rstrip()
        intfile.close()
    with open(output_path / output_name, 'w') as f:
        for root, dirs, files in os.walk(img_path):
            rel_dir = Path(os.path.relpath(root, img_path))
            for filename in files:
                f.write(str(rel_dir / filename) + ' ' + intrins_param + '\n')
        f.close()
        print('queries with intrinsics file has been saved in ' +
              str(output_path) + '/' + str(output_name) + "'.")
