from .cal_metric import call_TEDS, call_BLEU, call_METEOR, call_Edit_dist, call_CDM

from registry.registry import METRIC_REGISTRY

__all__ = [
    "call_TEDS",
    "call_BLEU",
    "call_METEOR",
    "call_Edit_dist",
    "call_CDM"
]

print('METRIC_REGISTRY: ', METRIC_REGISTRY.list_items())