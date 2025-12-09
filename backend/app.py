import os
import csv
from dotenv import load_dotenv

load_dotenv()

def ler_csv(caminho):
    with open(caminho, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for linha in reader:
            print(linha)

def main():
    arquivo_csv = os.getenv("CSV_PATH", "CAMINHO/PLACEHOLDER/ARQUIVO.csv")
    print(f"Lendo arquivo: {arquivo_csv}")
    ler_csv(arquivo_csv)

if __name__ == "__main__":
    main()
