import os
import sys
import logging

#Log string format - timestamp, log level, filename message
logging_str = "[%(asctime)s] [%(levelname)s] [%(filename)s] %(message)s"

log_dir = "logs"
log_filepath = os.path.join(log_dir, "cnnClassifier.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("cnnClassifierLogger")