from pathlib import Path
import os
from hloc import extract_features, match_features, reconstruction, visualization, pairs_from_retrieval,pairs_from_exhaustive

outp = Path("PMUC_outputs")
for i in os.scandir('/src/matcher_engine/HierarchicalLocalization/PMUC_Dataset'):
    if os.path.exists(Path(i.path) / 'images' / 'db'):
        map_name = Path(i.name)
        images = Path(i.path) / "images"

        outputs = outp / map_name
        sfm_pairs = outputs / 'pairs-netvlad.txt'
        sfm_dir = outputs / 'sfm_superpoint+superglue'
        feature_path = outputs / 'feats-superpoint-n4096-r1024.h5'
        retrieval_path = outputs / 'openibl_4096.h5'
        match_path = outputs / "feats-superpoint-n4096-r1024_matches-superglue_pairs-custom_retrieved.h5"
        retrieval_conf = extract_features.confs['netvlad']
        feature_conf = extract_features.confs['superpoint_aachen']
        matcher_conf = match_features.confs['superglue']

        retrieval_path = extract_features.main(retrieval_conf, images, outputs)

        if "isl" in str(map_name): num_matched = 48
        else: num_matched = 50
        pairs_from_retrieval.main(retrieval_path, sfm_pairs, num_matched=num_matched)

        feature_path = extract_features.main(feature_conf, images, outputs)
        match_path = match_features.main(matcher_conf, sfm_pairs, feature_conf['output'], outputs)

        # model = reconstruction.main(sfm_dir, images, sfm_pairs, feature_path, match_path)
