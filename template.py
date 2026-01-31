import os
import pathlib
from pathlib import Path   
import logging

logging .basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_namae ="datascience" 


list_of_files=[
    "github/workflows/.gitkeep",
    f"src/{project_namae}/__init__.py",
    f"src/{project_namae}/components/__init__.py",
    f"src/{project_namae}/utils/__init__.py",
    f"src/{project_namae}/config/common.py",
    f"src/{project_namae}/config/configuration.py",
    f"src/{project_namae}/pipeline/__init__.py",
    f"src/{project_namae}/entity/__init__.py",
    f"src/{project_namae}/constants/__init__.py",
    f"src/{project_namae}/entity/config_entity.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "Dockerfile",
    "setup.py",
    "reseach/research.ipynb",
    "template/index.html",
    "app.py"


]



for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory:{filedir} for file :{filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize (filepath)==0):
        with open (filepath,"w") as fp:
            pass
        logging.info (f"Creating file :{filepath}")
    else:
        logging.info (f"File :{filepath} already exists")

