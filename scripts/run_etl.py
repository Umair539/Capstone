from src.extract.extract import extract_data
from src.transform.transform import transform_data
from src.load.load import load_raw_data
from src.load.load import load_transformed_data
from src.utils.logging_utils import setup_logger

def main():
    # Setup ETL pipeline logger   
    logger = setup_logger("etl_pipeline", "etl_pipeline.log")

    try:
        extracted_data = extract_data()

        load_raw_data(extracted_data)

        transformed_data = transform_data(extracted_data)

        load_transformed_data(transformed_data)
        
    except Exception as e:
        logger.error(f"ETL pipeline failed: {e}")

if __name__ == "__main__":
    main()
