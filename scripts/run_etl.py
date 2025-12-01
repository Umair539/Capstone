from src.extract.extract import extract_data
from src.transform.transform import transform_data
from src.load.load import load_raw_data
from src.load.load import load_transformed_data

extracted_data = extract_data()

load_raw_data(extracted_data)

transformed_data = transform_data(extracted_data)

load_transformed_data(transformed_data)
