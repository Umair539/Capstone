import pandas as pd
from src.extract.extract_mag import extract_mag
from src.extract.extract_plasma import extract_plasma

from src.utils.logging_utils import setup_logger

logger = setup_logger("extract_data", "extract_data.log")

mag_url = 'https://services.swpc.noaa.gov/products/solar-wind/mag-7-day.json'
plasma_url = 'https://services.swpc.noaa.gov/products/solar-wind/plasma-7-day.json'

def extract_data():
    try:
        mag = extract_mag(mag_url)
        plasma = extract_plasma(plasma_url)
    
        return (mag, plasma)
    
    except Exception as e:
        logger.error(f"Data extraction failed: {str(e)}")