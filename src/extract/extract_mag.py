import pandas as pd
from src.extract.extract_json import extract_json
import logging
from src.utils.logging_utils import setup_logger

# Configure the logger
logger = setup_logger(__name__, "extract_data.log", level=logging.DEBUG)

def extract_mag(mag_url):
    try:
        mag_json = extract_json(mag_url)
        return pd.DataFrame(mag_json[1:], columns=mag_json[0])
    except Exception as e:
        logger.error(f'Error retrieving mag data: {e}')