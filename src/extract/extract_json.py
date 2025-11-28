import requests
import logging
from src.utils.logging_utils import setup_logger

# Configure the logger
logger = setup_logger(__name__, "extract_data.log", level=logging.DEBUG)

def extract_json(url):
    try:
        #Fetch JSON data from NOAA and convert to DataFrame
        response = requests.get(url, timeout=10)
        #response.raise_for_status()
        return response.json()
    
    except Exception as e:
        logger.error(f'Error fetching json data from {url}: {e}')
