import os
import cv2
import torch
from ultralytics import YOLO
from pdf_extract_kit.registry import MODEL_REGISTRY
from pdf_extract_kit.utils.visualization import  visualize_bbox


@MODEL_REGISTRY.register('layout_detection_yolo')
class LayoutDetectionYOLO:
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

        # Load the YOLO model from the specified path
        self.model = YOLO(config['model_path'])

        # Set model parameters
        self.img_size = config.get('img_size', 1280)
        self.pdf_dpi = config.get('pdf_dpi', 200)
        self.conf_thres = config.get('conf_thres', 0.25)
        self.iou_thres = config.get('iou_thres', 0.45)
        self.visualize = config.get('visualize', False)

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
        results = []
        for idx, image in enumerate(images):
            result = self.model.predict(image, imgsz=self.img_size, conf=self.conf_thres, iou=self.iou_thres, verbose=False)[0]
            if self.visualize:
                if not os.path.exists(result_path):
                    os.makedirs(result_path)
                boxes = result.__dict__['boxes'].xyxy
                classes = result.__dict__['boxes'].cls
                vis_result = visualize_bbox(image, boxes, classes, self.id_to_names)

                # Determine the base name of the image
                if image_ids:
                    base_name = image_ids[idx]
                else:
                    base_name = os.path.basename(image)
                
                result_name = f"{base_name}_MFD.png"
                
                # Save the visualized result                
                cv2.imwrite(os.path.join(result_path, result_name), vis_result)
            results.append(result)
        return results