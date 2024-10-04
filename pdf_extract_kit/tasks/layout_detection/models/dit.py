import os
import cv2
import torch
import numpy as np
from PIL import Image

from pdf_extract_kit.registry.registry import MODEL_REGISTRY
from pdf_extract_kit.utils.visualization import visualize_bbox

from ultralytics.utils import TQDM

from .unilm_util.dit.model_init import DiTPredictor
from pdf_extract_kit.dataset.detection.layoutlmv3_dataset import Layoutlmv3Dataset
from pdf_extract_kit.dataset.detection.base_detection_dataloader import build_dataloader

@MODEL_REGISTRY.register("layout_detection_dit")
class LayoutDetectionDiT:
    def __init__(self, config):
        """
        Initialize the LayoutDetectionYOLO class.

        Args:
            config (dict): Configuration dictionary containing model parameters.
        """
        # Mapping from class IDs to class names
        self.id_to_names = {
            0: 'title', 
            1: 'plain text',
            2: 'abandon', 
            3: 'figure', 
            4: 'figure_caption', 
            5: 'table', 
            6: 'table_caption', 
            7: 'table_footnote', 
            8: 'isolate_formula', 
            9: 'formula_caption'
        }
        self.batch_size = config.get('batch_size', 1)
        self.score_thr = config.get('score_thr', 0.25)
        self.workers = config.get('workers', 4)
        self.visualize = config.get('visualize', False)
        self.model = DiTPredictor(
            weights = config.get('model_path', None), 
            score_thr = self.score_thr,
        )

    def predict(self, images, result_path, image_ids=None):
        """
        Predict layouts in images.

        Args:
            images (list): List of images to be predicted.
            result_path (str): Path to save the prediction results.
            image_ids (list, optional): List of image IDs corresponding to the images.

        Returns:
            list: List of prediction results.
        """
        if not os.path.exists(result_path):
            os.makedirs(result_path)
            
        # dataset & dataloader
        self.dataset = Layoutlmv3Dataset(image_list = images)
        self.dataloader = build_dataloader(
            self.dataset, 
            self.batch_size, 
            self.workers, 
            shuffle=False, 
            rank=-1
        )
        
        # batch inference
        results = []
        bar = TQDM(self.dataloader, desc="Batch Inferencing ...", total=len(self.dataloader))
        for batch_i, batch in enumerate(bar):
            layout_res = self.model(batch["img"], ignore_catids=[])
            for im_file, layout_res_single in zip(batch["im_file"], layout_res):
                poly = np.array([det["poly"] for det in layout_res_single["layout_dets"]])
                boxes = poly[:, [0,1,4,5]] 
                scores = np.array([det["score"] for det in layout_res_single["layout_dets"]])
                classes = np.array([det["category_id"] for det in layout_res_single["layout_dets"]])
                
                if self.visualize:
                    vis_result = visualize_bbox(im_file, boxes, classes, scores, self.id_to_names)
                    # Determine the base name of the image
                    base_name = os.path.basename(im_file)
                    result_name = f"{base_name}_layout.png"
                    # Save the visualized result                
                    cv2.imwrite(os.path.join(result_path, result_name), vis_result)

                # append result
                results.append({
                    "im_path": im_file,
                    "boxes": boxes,
                    "scores": scores,
                    "classes": classes,
                })
        return results
