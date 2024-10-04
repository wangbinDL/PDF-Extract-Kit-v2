import os
import cv2
import torch
import numpy as np

from pdf_extract_kit.registry import MODEL_REGISTRY
from pdf_extract_kit.utils.visualization import visualize_bbox
from pdf_extract_kit.dataset.detection.yolo_dataset import YoloDataset
from pdf_extract_kit.dataset.detection.base_detection_dataloader import build_dataloader

from ultralytics.utils import TQDM, ops
from ultralytics.nn.autobackend import AutoBackend
from ultralytics.utils.torch_utils import select_device

@MODEL_REGISTRY.register('formula_detection_yolo')
class FormulaDetectionYOLO:
    def __init__(self, config):
        """
        Initialize the FormulaDetectionYOLO class.

        Args:
            config (dict): Configuration dictionary containing model parameters.
        """
        # Mapping from class IDs to class names
        self.id_to_names = {
            0: 'inline',
            1: 'isolated'
        }

        # Set model parameters
        self.img_size = config.get('img_size', 1280)
        self.conf_thres = config.get('conf_thres', 0.25)
        self.iou_thres = config.get('iou_thres', 0.45)
        self.visualize = config.get('visualize', False)
        self.rect = config.get('rect', True)
        self.device = config.get('device', 'cuda' if torch.cuda.is_available() else 'cpu')
        self.batch_size = config.get('batch_size', 1)
        self.max_det = config.get('max_det', 100)
        self.nc = config.get('nc', 2)
        self.workers = config.get('workers', 8)
        
        # Load the YOLO model from the specified path
        self.cur_device = select_device(self.device, self.batch_size)
        self.model = AutoBackend(
            weights=config['model_path'],
            device=self.cur_device,
            dnn=False,
            data=None,
            fp16=False,
        )

    def preprocess(self, batch):
        """Preprocesses batch of images for YOLO training."""
        batch["img"] = batch["img"].to(self.cur_device, non_blocking=True)
        batch["img"] = batch["img"].float() / 255
        for k in ["batch_idx"]:
            batch[k] = batch[k].to(self.cur_device)
        return batch
        
    def postprocess(self, preds):
        """Apply Non-maximum suppression to prediction outputs."""
        return ops.non_max_suppression(
            preds,
            self.conf_thres,
            self.iou_thres,
            labels=[],
            multi_label=True,
            agnostic=False,
            max_det=self.max_det,
        )
        
    def _prepare_batch(self, si, batch):
        """Prepares a batch of images and annotations for validation."""
        idx = batch["batch_idx"] == si
        ori_shape = batch["ori_shape"][si]
        imgsz = batch["img"].shape[2:]
        ratio_pad = batch["ratio_pad"][si]
        return {"ori_shape": ori_shape, "imgsz": imgsz, "ratio_pad": ratio_pad}

    def _prepare_pred(self, pred, pbatch):
        """Prepares a batch of images and annotations for validation."""
        predn = pred.clone()
        ops.scale_boxes(
            pbatch["imgsz"], predn[:, :4], pbatch["ori_shape"], ratio_pad=pbatch["ratio_pad"]
        )  # native-space pred
        return predn
        
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
        
        self.dataset = YoloDataset(
            image_list = images,
            imgsz = self.img_size,
            batch_size = self.batch_size,
            rect = self.rect,
        )
        self.dataloader = build_dataloader(self.dataset, self.batch_size, self.workers, shuffle=False, rank=-1)
        
        results = []  # empty before each val
        bar = TQDM(self.dataloader, desc="Batch Inferencing ...", total=len(self.dataloader))
        for batch_i, batch in enumerate(bar):
            # Preprocess
            batch = self.preprocess(batch)
            # Inference
            preds = self.model(batch["img"], augment=False)
            preds = self.postprocess(preds)

            for si, pred in enumerate(preds):
                pbatch = self._prepare_batch(si, batch)
                predn = self._prepare_pred(pred, pbatch)
                boxes = predn[:,:4].cpu().numpy()
                scores = predn[:,4].cpu().numpy()
                classes = predn[:,-1].cpu().numpy()
                    
                # append result
                results.append({
                    "im_path": batch['im_path'][si],
                    "boxes": boxes,
                    "scores": scores,
                    "classes": classes,
                })
                
                # visualize
                if self.visualize:
                    if not os.path.exists(result_path):
                        os.makedirs(result_path)
                    vis_result = visualize_bbox(batch["im_path"][si], boxes, classes, scores, self.id_to_names)
                    # Determine the base name of the image
                    base_name = os.path.basename(batch['im_path'][si])
                    result_name = f"{base_name}_MFD.png"
                    # Save the visualized result                
                    cv2.imwrite(os.path.join(result_path, result_name), vis_result)
                    
        return results