CUDA_VISIBLE_DEVICES=2 python scripts/layout_detection.py --config configs/layout_detection_layoutlmv3.yaml
CUDA_VISIBLE_DEVICES=2 python scripts/layout_detection.py --config configs/layout_detection_dit.yaml
CUDA_VISIBLE_DEVICES=0 python scripts/layout_detection.py --config configs/layout_detection_yolo.yaml