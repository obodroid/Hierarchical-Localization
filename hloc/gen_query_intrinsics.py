import os
from pathlib import Path
#path_query = Path('querySTNight')
#dbinfile = Path('outputs/sfm5/SFMrecons/db_with_intrinsics_m0.txt')
#outputpath = Path('outputs/sfm5/SFMLocSTnightretq5')
#outputname = "queries_with_intrinsics.txt"

def query_intrinsics(img_path,db_intrinsics_file,output_path,output_name):
    print('Creating lists of quries intrinsics...')
    file_list = os.listdir(img_path)
    with open(db_intrinsics_file) as intfile:
        intrins_param = intfile.readline().rstrip()
        intfile.close()
    with open(output_path / output_name, 'w') as f:
        for i in file_list:
            f.write(i + ' ' + intrins_param + '\n')
        f.close()
        print('a file has been saved in ' + "'" + str(output_path) + '/' + str(output_name) + "'.")

#query_intrinsics(path_query,dbinfile,outputpath,outputname)
