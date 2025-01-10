import os
import yaml
from src.datascience import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns a ConfigBox object."""
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            config = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} lodded succesfully")
            return ConfigBox(config)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_dir: list, verbose = True):
    


    for path in path_to_dir:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Directory {path} created succesfully")


@ensure_annotations
def save_json(path_to_json: Path, data: dict):

    with open(path_to_json, 'w') as json_file:
        json.dump(data,json_file,indent=4)

    logger.info(f"json file saved at:{path_to_json}")


@ensure_annotations
def load_json(path_to_json: Path) -> ConfigBox:

    with open(path_to_json) as f:
        content = json.load(f)
    
    logger.info(f"json file loaded sucessfully from: {path_to_json}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path = Path):
    joblib.dump(value = data, filename = path)
    logger.info(f"bin file saved at:{path}")



@ensure_annotations
def load_bin(path: Path) -> Any:
    data = joblib.load(path)
    logger.info("binary file loaded from {path}")
    return data


