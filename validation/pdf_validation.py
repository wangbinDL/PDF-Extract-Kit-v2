# coding: utf-8
import os
import argparse
import sys
import io
import os
import pathlib
import sys
import yaml
from registry.registry import EVAL_TASK_REGISTRY, DATASET_REGISTRY, METRIC_REGISTRY
import dataset
import task
import metrics

print(DATASET_REGISTRY.list_items())

def process_args(args):
    parser = argparse.ArgumentParser(description='Render latex formulas for comparison.')
    parser.add_argument('--config', '-c', type=str, default='')
    parameters = parser.parse_args(args)
    return parameters

if __name__ == '__main__':
    parameters = process_args(sys.argv[1:])
    config_path = parameters.config
    
    if isinstance(config_path, (str, pathlib.Path)):
        with io.open(os.path.abspath(config_path), "r", encoding="utf-8") as f:
            cfg = yaml.load(f, Loader=yaml.FullLoader)
    else:
        raise TypeError("Unexpected file type")

    if cfg is not None and not isinstance(cfg, (list, dict, str)):
        raise IOError(  # pragma: no cover
            f"Invalid loaded object type: {type(cfg).__name__}"
        )

    # print(cfg['tasks'])

    for task in cfg['tasks']:
        if not cfg.get(task):
            print('No config for task {task}')
        dataset = cfg[task]['dataset']['dataset_name']
        # metrics_list = [METRIC_REGISTRY.get(i) for i in cfg[task]['metrics']] # TODO: 直接在主函数里实例化
        metrics_list = cfg[task]['metrics']  # 在task里再实例化
        val_dataset = DATASET_REGISTRY.get(dataset)(cfg[task])
        val_task = EVAL_TASK_REGISTRY.get(task)
        val_task(val_dataset, metrics_list)
