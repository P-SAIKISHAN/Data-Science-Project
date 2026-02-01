import os
import yaml
from src.datascience.utils import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox   
from typing import Any
from pathlib import Path
from box.exceptions import BoxValueError


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a yaml file and returns a ConfigBox object

    Args:
        path_to_yaml (Path): path to the yaml file

    Returns:
        ConfigBox: ConfigBox object containing the yaml file data
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
        logger.info(f"yaml file: {path_to_yaml} loaded successfully")
        return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates list of directories

    Args:
        path_to_directories (list[Path]): list of paths to directories
        verbose (bool, optional): log directory creation. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose: 
            logger.info(f"created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """Saves a dictionary to a json file

    Args:
        path (Path): path to the json file
        data (dict): data to be saved
    """
    with open(path, "w") as json_file:
        json.dump(data, json_file, indent=4)
    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Loads a json file and returns a ConfigBox object

    Args:
        path (Path): path to the json file

    Returns:
        ConfigBox: ConfigBox object containing the json file data
    """
    with open(path, "r") as json_file:
        content = json.load(json_file)

    logger.info(f"json file loaded from: {path}")   
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path) -> None:
    """Saves data to a binary file using joblib

    Args:
        data (Any): data to be saved
        path (Path): path to the binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """Loads data from a binary file using joblib
    
    Args:
        path (Path): path to the binary file

    Returns:
        Any: data loaded from the binary file    
    """
    data = joblib.load(filename=path)
    logger.info(f"binary file loaded from: {path}")
    return data