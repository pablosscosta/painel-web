import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    CSV_PATH = os.getenv("CSV_PATH", "CAMINHO/PLACEHOLDER/ARQUIVO.csv")
    FLASK_DEBUG = os.getenv("FLASK_DEBUG", "True").lower() == "true"

config = Config()