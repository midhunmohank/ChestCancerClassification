import os
from pathlib import Path
from typing import Any
import base64
import yaml
import json

from cnnClassifier import logger
import joblib
from ensure import ensure_annotations
from box import config_box, ConfigBox

from box.exceptions import BoxValueError



@ensure_annotations
def read_yaml(path_to_yaml: Path)-> ConfigBox:
    """
    Read a yaml file and return a ConfigBox object.
    """
    try:
        with open(path_to_yaml, 'r') as file:
            config = yaml.safe_load(file)
            logger.info(f"Read the yaml file from {path_to_yaml}")
        return config_box(config)
    except BoxValueError as e:
        logger.error(f"Error reading the yaml file from {path_to_yaml}")
        raise e
    except Exception as e:
        logger.error(f"Error reading the yaml file from {path_to_yaml}")
        raise e
    
@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Save a binary file.
    """
    try:
        with open(path, 'wb') as file:
            joblib.dump(data, file)
            logger.info(f"Saved the binary file to {path}")
    except Exception as e:
        logger.error(f"Error saving the binary file to {path}")
        raise e
    
@ensure_annotations
def load_bin(path: Path)-> Any:
    """
    Load a binary file.
    """
    try:
        data = joblib.load(path)
        logger.info(f"Loaded the binary file from {path}")
        return data
    except Exception as e:
        logger.error(f"Error loading the binary file from {path}")
        raise e
    
@ensure_annotations
def get_size(path: Path) -> str:
    size = round(os.path.getsize(path) / 1024, 2)
    return f"{size} KB"


def decodeImage(imgString, fileName):
    imgdata = base64.b64decode(imgString)
    with open(fileName, 'wb') as file:
        file.write(imgdata)
        file.close()

def encodeImage(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read())
    
    

    

