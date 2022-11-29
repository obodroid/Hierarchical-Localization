import subprocess

def automatic_reconstructor(workspace_path, image_path):
    subprocess.run("colmap automatic_reconstructor --workspace_path {} --image_path {}".format(workspace_path, image_path))
def bundle_adjuster(input_path, output_path):
    subprocess.run("colmap bundle_adjuster --input_path {} --output_path {}".format(input_path, output_path))
def color_extractor(image_path, input_path, output_path):
    subprocess.run("colmap color_extractor --image_path {} --input_path {} --outputs_path {}".format(image_path, input_path, output_path))
def database_cleaner(type, database_path):
    subprocess.run("colmap database_cleaner --type {} --database_path {}".format(type, database_path))
def database_creator(database_path):
    subprocess.run("colmap database_creator --database_path {}".format(database_path))
def database_merger(database_path1, database_path2, merged_database_path):
    subprocess.run("colmap database_merger --database_path1 {} --database_path2 {} --merged_database_path {}".format(database_path1, database_path2, merged_database_path))
def delaunay_mesher(input_path, input_type, output_path):
    subprocess.run("colmap delaunay_mesher --input_path {} --input_type {} --output_path {}".format(input_path, input_type, output_path))
def exhaustive_matcher(database_path):
    subprocess.run("colmap exhaustive_matcher --database_path {}".format(database_path))
def feature_extractor(database_path, image_path):
    subprocess.run("colmap feature_extractor --database_path {} --image_path {}".format(database_path, image_path))
def feature_importer(database_path, image_path, import_path):
    subprocess.run("colmap feature_importer --database_path {} --image_path {} --import_path {}".format(database_path, image_path, import_path))
def hierarchical_mapper(database_path, image_path, output_path):
    subprocess.run("colmap hierarchical_mapper --database_path {} --image_path {} --output_path {}".format(database_path, image_path, output_path))
def image_deleter(input_path, output_path, image_ids_path, image_names_path):
    subprocess.run("colmap image_deleter --input_path {} --output_path {} --image_ids_path {} --image_names_path {}".format(input_path, output_path, image_ids_path, image_names_path))
def image_filterer(input_path, output_path):
    subprocess.run("colmap image_filterer --input_path {} --output_path {}".format(input_path, output_path))
def image_rectifier(image_path, input_path, output_path, stereo_pairs_list):
    subprocess.run("colmap image_rectifier --image_path {} --input_path {} --output_path {} --stereo_pairs_list {}".format(image_path, input_path, output_path, stereo_pairs_list))
def image_registrator(database_path, input_path, output_path):
    subprocess.run("colmap image_registrator --database_path {} --input_path {} --output_path {}".format(database_path, input_path, output_path))
def image_undistorter(image_path, input_path, output_path, output_type, image_list_path):
    subprocess.run("colmap image_undistorter --image_path {} --input_path {} --output_path {} --output_type {} --image_list_path {}".format(image_path, input_path, output_path, output_type, image_list_path))
def image_undistorter_standalone(image_path, input_file, output_path):
    subprocess.run("colmap image_undistorter_standalone --image_path {} --input_file {} --output_path {}".format(image_path, input_file, output_path))
def mapper(database_path, image_path, input_path, output_path):
    subprocess.run("colmap mapper --database_path {} -- image_path {} --input_path {} --output_path {}".format(database_path, image_path, input_path, output_path))
def matches_importer(database_path, match_list_path, match_type):
    subprocess.run("colmap matches_importer --database_path {} --match_list_path {} --match_type {}".format(database_path, match_list_path, match_type))
def model_aligner(input_path, output_path, ref_images_path, alignment_type):
    subprocess.run("colmap model_aligner --input_path {} --output_path {} --ref_images_path {} --alignment_type {} --robust_alignment 1.0 --robust_alignment_max_error 3.0".format(input_path, output_path, ref_images_path, alignment_type))
def model_analyzer(input_path):
    subprocess.run("colmap model_analyzer --path {}".format(input_path))
def model_comparer(input_path1, input_path2, output_path):
    subprocess.run("colmap model_comparer --input_path1 {} --input_path2 {} --output_path {}".format(input_path1,input_path2, output_path))
def model_converter(input_path, output_path, output_type):
    subprocess.run("colmap model_converter --input_path {} --output_path {} --output_type {}".format(input_path, output_path, output_type))
def model_cropper(input_path, output_path, boundary, gps_transform_path):
    subprocess.run("colmap model_cropper --input_path {} --output_path {} --boundary {} --gps_transform_path {}".format(input_path, output_path, boundary, gps_transform_path))
def model_merger(input_path1, input_path2, output_path):
    subprocess.run("colmap model_merger --input_path1 {} --input_path2 {} --output_path {}".format(input_path1, input_path2, output_path))
def model_orientation_aligner(image_path, input_path, output_path, method):
    subprocess.run("colmap model_orientation_aligner --image_path {} --input_path {} --output_path {} --method {}".format(image_path, input_path, output_path, method))

