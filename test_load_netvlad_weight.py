
from pathlib import Path

from hloc import extract_features, match_features, reconstruction, visualization, pairs_from_retrieval,pairs_from_exhaustive

images = Path('/src/matcher_engine/HierarchicalLocalization/datasets/canteen-20221115/images')

outputs = Path('/src/matcher_engine/HierarchicalLocalization/outputs/canteen-20221115-test/')
sfm_pairs = outputs / 'pairs-netvlad.txt'
sfm_dir = outputs / 'sfm_superpoint+superglue'
feature_path = outputs / 'feats-superpoint-n4096-r1024.h5'
retrieval_path = outputs / 'openibl_4096.h5'
match_path = outputs / "feats-superpoint-n4096-r1024_matches-superglue_pairs-custom_retrieved.h5"
retrieval_conf = extract_features.confs['netvlad']
feature_conf = extract_features.confs['superpoint_aachen']
matcher_conf = match_features.confs['superglue']

retrieval_path = extract_features.main(retrieval_conf, images, outputs)
pairs_from_retrieval.main(retrieval_path, sfm_pairs, num_matched=5)