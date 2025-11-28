import pandas as pd
from src.extract.extract_json import extract_json
import logging
from src.utils.logging_utils import setup_logger

# Configure the logger
logger = setup_logger(__name__, "extract_data.log", level=logging.DEBUG)

def extract_plasma(plasma_url):
    try:
        plasma_json = extract_json(plasma_url)
        return pd.DataFrame(plasma_json[1:], columns=plasma_json[0])
    except Exception as e:
        logger.error(f'Error retrieving mag data: {e}')