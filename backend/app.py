import os
import csv
from flask import Flask, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

def ler_arquivo():
    caminho = os.getenv("CSV_PATH", "CAMINHO/PLACEHOLDER/ARQUIVO.csv")
    dados = []
    try:
        with open(caminho, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for linha in reader:
                # pega apenas o primeiro valor da linha
                if linha:  
                    dados.append(linha[0])
    except Exception as e:
        print(f"Erro ao ler arquivo: {e}")
    return dados


@app.route("/api/dados", methods=["GET"])
def api_dados():
    dados = ler_arquivo()
    return jsonify(dados)

if __name__ == "__main__":
    app.run(debug=True)

