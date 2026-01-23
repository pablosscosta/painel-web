import os
import csv
from config import config

def ler_arquivo():

    caminho = config.CSV_PATH
    dados = []
    
    try:
        with open(caminho, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for linha in reader:
                if linha:
                    dados.append(linha[0])
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho}")
    except Exception as e:
        print(f"Erro ao ler arquivo: {e}")
    
    return dados, caminho