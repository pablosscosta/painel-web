from flask import jsonify
from file_reader import ler_arquivo
from datetime import datetime
import os

def api_dados():
    dados, caminho = ler_arquivo()

    try:
        timestamp = os.path.getmtime(caminho)
        modificado = datetime.fromtimestamp(timestamp).strftime("%d/%m/%Y %H:%M")
    except Exception:
        modificado = "desconhecido"

    return jsonify({
        "valor": dados[0] if dados else None,
        "modificado": modificado
    })