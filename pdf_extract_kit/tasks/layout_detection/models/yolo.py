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
        
        # Set model parameters
        self.img_size = config.get('img_size', 1280)
        self.conf_thres = config.get('conf_thres', 0.25)
        self.iou_thres = config.get('iou_thres', 0.45)
        self.visualize = config.get('visualize', False)
        self.rect = config.get('rect', True)
        self.device = config.get('device', 'cuda' if torch.cuda.is_available() else 'cpu')
        self.batch_size = config.get('batch_size', 1)
        self.max_det = config.get('max_det', 300)
        self.nc = config.get('nc', 10)
        self.workers = config.get('workers', 8)
        self.nms = config.get('nms', False)
        
        if self.nms:
            import torchvision
            self.nms_func = torchvision.ops.nms
        
        # Load the YOLO model from the specified path
        self.cur_device = select_device(self.device, self.batch_size)
        self.model = AutoBackend(
            weights=config['model_path'],
            device=self.cur_device,
            dnn=False,
            data=None,
            fp16=False,
            fuse=False,
        )

    def preprocess(self, batch):
        """Preprocesses batch of images for YOLO training."""
        batch["processed_img"] = batch["img"].to(self.cur_device, non_blocking=True)
        batch["processed_img"] = batch["processed_img"].float() / 255
        for k in ["batch_idx"]:
            batch[k] = batch[k].to(self.cur_device)
        return batch
        
    def postprocess(self, preds, conf=None):
        if isinstance(preds, dict):
            preds = preds["one2one"]

        if isinstance(preds, (list, tuple)):
            preds = preds[0]
        
        preds = preds.transpose(-1, -2)
        boxes, scores, labels = ops.v10postprocess(preds, self.max_det, self.nc)
        bboxes = ops.xywh2xyxy(boxes)
        
        preds = torch.cat([bboxes, scores.unsqueeze(-1), labels.unsqueeze(-1)], dim=-1)
        if preds.shape[-1] == 6 and conf is not None:  # end-to-end model (BNC, i.e. 1,300,6)
            preds = [pred[pred[:, 4] > conf] for pred in preds]
        return preds
        
    def _prepare_batch(self, si, batch):
        """Prepares a batch of images and annotations for validation."""
        idx = batch["batch_idx"] == si
        ori_shape = batch["ori_shape"][si]
        imgsz = batch["img"].shape[2:]
        ratio_pad = batch["ratio_pad"][si]
        return dict(ori_shape=ori_shape, imgsz=imgsz, ratio_pad=ratio_pad)

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
            preds = self.model(batch["processed_img"], augment=False)
            preds = self.postprocess(preds, conf=self.conf_thres)

            for si, pred in enumerate(preds):
                pbatch = self._prepare_batch(si, batch)
                predn = self._prepare_pred(pred, pbatch)
                boxes = predn[:,:4].cpu().numpy()
                scores = predn[:,4].cpu().numpy()
                classes = predn[:,-1].cpu().numpy()
            
                if self.nms:
                    indices = self.nms_func(boxes=torch.Tensor(boxes), scores=torch.Tensor(scores),iou_threshold=self.iou_thres)
                    boxes, scores, classes = boxes[indices], scores[indices], classes[indices]
                    if len(boxes.shape) == 1:
                        boxes = np.expand_dims(boxes, 0)
                        scores = np.expand_dims(scores, 0)
                        classes = np.expand_dims(classes, 0)
                    
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
                    result_name = f"{base_name}_layout.png"
                    # Save the visualized result                
                    cv2.imwrite(os.path.join(result_path, result_name), vis_result)
                    
        return results