import logging
import os
from config.settings import LOG_DIR

os.makedirs(LOG_DIR, exist_ok=True)

def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[
            logging.FileHandler(f"{LOG_DIR}/email_pipeline.log", encoding="utf-8"),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger("email_pipeline")
