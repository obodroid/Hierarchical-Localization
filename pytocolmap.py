import subprocess

def automatic_reconstructor(workspace_path, image_path):
    subprocess.run("colmap automatic_reconstructor --workspace_path {} --image_path {}".format(workspace_path, image_path), shell=True)
def bundle_adjuster(input_path, output_path):
    subprocess.run("colmap bundle_adjuster --input_path {} --output_path {}".format(input_path, output_path), shell=True)
def color_extractor(image_path, input_path, output_path):
    subprocess.run("colmap color_extractor --image_path {} --input_path {} --outputs_path {}".format(image_path, input_path, output_path), shell=True)
def database_cleaner(type, database_path):
    subprocess.run("colmap database_cleaner --type {} --database_path {}".format(type, database_path), shell=True)
def database_creator(database_path):
    subprocess.run("colmap database_creator --database_path {}".format(database_path), shell=True)
def database_merger(database_path1, database_path2, merged_database_path):
    subprocess.run("colmap database_merger --database_path1 {} --database_path2 {} --merged_database_path {}".format(database_path1, database_path2, merged_database_path), shell=True)
def delaunay_mesher(input_path, input_type, output_path):
    subprocess.run("colmap delaunay_mesher --input_path {} --input_type {} --output_path {}".format(input_path, input_type, output_path), shell=True)
def exhaustive_matcher(database_path):
    subprocess.run("colmap exhaustive_matcher --database_path {}".format(database_path), shell=True)
def feature_extractor(database_path, image_path):
    subprocess.run("colmap feature_extractor --database_path {} --image_path {}".format(database_path, image_path), shell=True)
def feature_importer(database_path, image_path, import_path):
    subprocess.run("colmap feature_importer --database_path {} --image_path {} --import_path {}".format(database_path, image_path, import_path), shell=True)
def hierarchical_mapper(database_path, image_path, output_path):
    subprocess.run("colmap hierarchical_mapper --database_path {} --image_path {} --output_path {}".format(database_path, image_path, output_path), shell=True)
def image_deleter(input_path, output_path, image_ids_path, image_names_path):
    subprocess.run("colmap image_deleter --input_path {} --output_path {} --image_ids_path {} --image_names_path {}".format(input_path, output_path, image_ids_path, image_names_path), shell=True)
def image_filterer(input_path, output_path):
    subprocess.run("colmap image_filterer --input_path {} --output_path {}".format(input_path, output_path), shell=True)
def image_rectifier(image_path, input_path, output_path, stereo_pairs_list):
    subprocess.run("colmap image_rectifier --image_path {} --input_path {} --output_path {} --stereo_pairs_list {}".format(image_path, input_path, output_path, stereo_pairs_list), shell=True)
def image_registrator(database_path, input_path, output_path):
    subprocess.run("colmap image_registrator --database_path {} --input_path {} --output_path {}".format(database_path, input_path, output_path), shell=True)
def image_undistorter(image_path, input_path, output_path, output_type, image_list_path):
    subprocess.run("colmap image_undistorter --image_path {} --input_path {} --output_path {} --output_type {} --image_list_path {}".format(image_path, input_path, output_path, output_type, image_list_path), shell=True)
def image_undistorter_standalone(image_path, input_file, output_path):
    subprocess.run("colmap image_undistorter_standalone --image_path {} --input_file {} --output_path {}".format(image_path, input_file, output_path), shell=True)
def mapper(database_path, image_path, input_path, output_path):
    subprocess.run("colmap mapper --database_path {} -- image_path {} --input_path {} --output_path {}".format(database_path, image_path, input_path, output_path), shell=True)
def matches_importer(database_path, match_list_path, match_type):
    subprocess.run("colmap matches_importer --database_path {} --match_list_path {} --match_type {}".format(database_path, match_list_path, match_type), shell=True)
def model_aligner(input_path, output_path, ref_images_path, alignment_type):
    subprocess.run("colmap model_aligner --input_path {} --output_path {} --ref_images_path {} --alignment_type {} --robust_alignment 1.0 --robust_alignment_max_error 3.0".format(input_path, output_path, ref_images_path, alignment_type), shell=True)
def model_analyzer(input_path):
    subprocess.run("colmap model_analyzer --path {}".format(input_path), shell=True)
def model_comparer(input_path1, input_path2, output_path):
    subprocess.run("colmap model_comparer --input_path1 {} --input_path2 {} --output_path {}".format(input_path1,input_path2, output_path), shell=True)
def model_converter(input_path, output_path, output_type):
    subprocess.run("colmap model_converter --input_path {} --output_path {} --output_type {}".format(input_path, output_path, output_type), shell=True)
def model_cropper(input_path, output_path, boundary, gps_transform_path):
    subprocess.run("colmap model_cropper --input_path {} --output_path {} --boundary {} --gps_transform_path {}".format(input_path, output_path, boundary, gps_transform_path), shell=True)
def model_merger(input_path1, input_path2, output_path):
    subprocess.run("colmap model_merger --input_path1 {} --input_path2 {} --output_path {}".format(input_path1, input_path2, output_path), shell=True)
def model_orientation_aligner(image_path, input_path, output_path, method):
    subprocess.run("colmap model_orientation_aligner --image_path {} --input_path {} --output_path {} --method {}".format(image_path, input_path, output_path, method), shell=True)
def model_splitter(input_path, output_path, split_type):
    subprocess.run("colmap model_splitter --input_path {} --output_path {} --split_type {}".format(input_path, output_path, split_type), shell=True)
def model_transformer(input_path, output_path, transform_path):
    subprocess.run("colmap model_transformer --input_path {} --output_path {} --transform_path {}".format(input_path, output_path, transform_path), shell=True)
def point_triangulator(image_path, input_path, output_path):
    subprocess.run("colmap point_triangulator --image_path {} --input_path {} --output_path {}".format(image_path, input_path, output_path), shell=True)
def poisson_mesher(input_path, output_path):
    subprocess.run("colmap poisson_mesher --input_path {} --output_path {}".format(input_path, output_path), shell=True)
def project_generator(project_path, output_path, quality):
    subprocess.run("colmap project_generator --project_path {} --output_path {} --quality {}".format(project_path, output_path, quality), shell=True)
def rig_bundle_adjuster(input_path, output_path, rig_config_path):
    subprocess.run("colmap rig_bundle_adjuster --input_path {} --output_path {} --rig_config_path {}".format(input_path, output_path, rig_config_path), shell=True)
def sequential_matcher(database_path):
    subprocess.run("colmap sequential_matcher --database_path {}".format(database_path), shell=True)
def spatial_matcher(database_path):
    subprocess.run("colmap spatial_matcher --database_path {}".format(database_path), shell=True)
def stereo_fusion(workspace_path, output_path):
    subprocess.run("colmap stereo_fusion --workspace_path {} --output_path {}".format(workspace_path, output_path), shell=True)
def transitive_matcher(database_path):
    subprocess.run("colmap transitive_matcher --database_path {}".format(database_path), shell=True)
def vocab_tree_builder(database_path, vocab_tree_path):
    subprocess.run("colmap vocab_tree_builder --database_path {} --vocab_tree_path {}".format(database_path, vocab_tree_path), shell=True)
def vocab_tree_matcher(database_path, vocab_tree_path, match_list_path):
    subprocess.run("colmap vocab_tree_matcher --database_path {} --VocabTreeMatching.vocab_tree_path {} --VocabTreeMatching.match_list_path {}".format(database_path, vocab_tree_path, match_list_path), shell=True)
def vocab_tree_retriever(database_path, vocab_tree_path, database_image_list_path, query_image_list_path, output_index_path):
    subprocess.run("colmap vocab_tree_retriever --database_path {} --vocab_tree_path {} --database_image_list_path {} --query_image_list_path {} --output_index_path {}".format(database_path, vocab_tree_path, database_image_list_path, query_image_list_path, output_index_path), shell=True)

