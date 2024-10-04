# -*- coding: utf-8 -*-
# Copyright (c) Facebook, Inc. and its affiliates.

import cv2

from .base_detection_dataset import BaseDetectionDataset

class Layoutlmv3Dataset(BaseDetectionDataset):
    def __init__(self, image_list):
        super().__init__(image_list=image_list)
        
    def load_image(self, i):
        """Loads 1 image from dataset index 'i', returns (im, resized hw)."""
        f = self.im_files[i]
        im = cv2.imread(f)  # BGR
        if im is None:
            raise FileNotFoundError(f"Image Not Found {f}")
        h0, w0 = im.shape[:2]  # orig hw
        return im, (h0, w0), im.shape[:2]
        
    def collate_fn(self, batch):
        """Collates data samples into batches."""
        new_batch = {
            "img": [b["img"] for b in batch],
            "im_file": [b["im_path"] for b in batch],
        }
        return new_batch