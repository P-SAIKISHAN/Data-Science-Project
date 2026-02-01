import logging
from pathlib import Path

# Create logs directory if it doesn't exist
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s]: %(levelname)s: %(module)s: %(message)s',
    handlers=[
        logging.FileHandler(log_dir / "running_logs.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("datascience")