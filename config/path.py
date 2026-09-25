import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_RAW_PATH = os.path.join(BASE_DIR, "data", "raw", "car-price.csv")
DATA_PROCESSED_PATH = os.path.join(BASE_DIR, "data", "processed", "voiture_data_cleaned.csv")

PRE_TRAINED_MODEL_RESULTS_PATH = os.path.join(BASE_DIR, "models", 'results' , "pre_trained_model_results.csv")
HYPERPARAMETER_OPTIMIZATION_RESULTS_PATH = os.path.join(BASE_DIR, "models", 'results' , "hyperparameter_optimization_results.csv")

BEST_MODEL_PATH = os.path.join(BASE_DIR, "saved_models", 'best_model', "best_model.pkl")