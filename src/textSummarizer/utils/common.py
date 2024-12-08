''' Frequently used functions will be listed here '''

import os
from box.exceptions import BoxValueError
import yaml
from src.textSummarizer.logging import logger # custom logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


''' NOTE: ensure_annotations -> prevents a function to return undesirable output, it ensures that all given constraints are satisfied then only output will be shown '''
# function is responsible for reading a yaml file
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox: #ConfigBox enables to acess dict elements directly using . instead [] eg. d[key] = value == d.key
    """reads yaml file and return 
    
    Args:
        path_to_yaml(str): path like i/p
    
    Raises:
        valueError: if yaml file is empty
        e: empty file
    
    Returns: 
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


# responsible for creating directories, instead of manually creating directories we can make use of this utility function
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """ create list of directories
    
    Args: 
        path_to_directories (list): list of path to directories
        ignore_log (bool, optional): ignore if multiple dires is to be created, Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created new directory at: {path}")
            
            

# to find size of file in KBs
@ensure_annotations
def get_size(path: Path) -> str:
    """ get file size in KB
    Args:
        path(path): path of file
    Returns: 
        size in KB (str)
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


