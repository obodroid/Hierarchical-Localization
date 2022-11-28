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
def