import os
from pathlib import Path
import logging # to log all info during runtime

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "text-summarizer"

files_list = [ 
    ".github/workflows/.gitkeep", # used to write yaml file
    f"src/{project_name}/__init__.py", # to use classes define here in another files
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py", # comman utilities which can be used in multiple files will be saved here
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml", # model related parameters will be stored here
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for filepath in files_list:
    filepath = Path(filepath) # detects os type and converts the filepath to corresponding path-form
    # separating filea and their directory
    filedir, filename = os.path.split(filepath)

    # create directories if filedir is not empty
    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory: {filedir} for file: {filename}")

    # file exists or file has some code then ignore it
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"creating an empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists and is non-empty")
