from pathlib import Path

# Navigate from src/datascience/constants/__init__.py to project root
# __file__ is at: src/datascience/constants/__init__.py
# .parent = src/datascience/constants/
# .parent.parent = src/datascience/
# .parent.parent.parent = src/
# .parent.parent.parent.parent = project root
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent

CONFIG_FILE_PATH = PROJECT_ROOT / "config" / "config.yaml"
PARAMS_FILE_PATH = PROJECT_ROOT / "config" / "params.yaml"  
SCHEMA_FILE_PATH = PROJECT_ROOT / "config" / "schema.yaml"

# Debug print (you can remove this later)
print(f"PROJECT_ROOT: {PROJECT_ROOT}")
print(f"CONFIG exists: {CONFIG_FILE_PATH.exists()}")