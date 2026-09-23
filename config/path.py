import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_RAW_PATH = os.path.join(BASE_DIR, "data", "raw", "car-price.csv")
DATA_PROCESSED_PATH = os.path.join(BASE_DIR, "data", "processed", "voiture_data_cleaned.csv")