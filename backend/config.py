import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    CSV_PATH = os.getenv("CSV_PATH", "CAMINHO/PLACEHOLDER/ARQUIVO.csv")
    NOME_DESENVOLVEDOR = os.getenv("NOME_DESENVOLVEDOR", "Nome da Equipe de Desenvolvimento")
    NOME_FABRICA = os.getenv("NOME_FABRICA", "Nome da Fábrica")
    FLASK_DEBUG = os.getenv("FLASK_DEBUG", "True").lower() == "true"

config = Config()