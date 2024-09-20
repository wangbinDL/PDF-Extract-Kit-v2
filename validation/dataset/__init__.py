from .recog_dataset import RecognitionFormulaDataset
from .end2end_dataset import End2EndDataset
from .detection_dataset import DetectionDataset
from registry.registry import DATASET_REGISTRY

__all__ = [
    "RecognitionFormulaDataset",
    "End2EndDataset",
    "DetectionDataset"
]

print('DATASET_REGISTRY: ', DATASET_REGISTRY.list_items())