import pandas as pd
from src.transform.process_solar_wind import process_solar_wind
from src.transform.aggregate_solar_wind import aggregate_solar_wind
from src.utils.logging_utils import setup_logger

logger = setup_logger("transform_data", "transform_data.log")

def transform_data(extracted_data):
    try:
        mag, plasma = extracted_data
        solar = process_solar_wind(mag, plasma)
        solar_agg = aggregate_solar_wind(solar)
        
        return (solar, solar_agg)
    except Exception as e:
        logger.error(f"Data transformation failed: {str(e)}")