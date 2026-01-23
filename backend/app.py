import os
import csv
import time
from flask import Flask, jsonify, send_from_directory, Response, redirect
from datetime import datetime
from config import config
from file_reader import ler_arquivo

app = Flask(__name__, static_folder="../frontend", static_url_path="")


@app.route("/api/dados", methods=["GET"])
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

@app.route("/stream")
def stream():
    def gerar_eventos():
        ultimo_valor = None
        while True:
            dados, caminho = ler_arquivo()
            valor = dados[0] if dados else None
            try:
                timestamp = os.path.getmtime(caminho)
                modificado = datetime.fromtimestamp(timestamp).strftime("%d/%m/%Y %H:%M")
            except Exception:
                modificado = "desconhecido"

            if valor != ultimo_valor:
                yield f'data: {{"valor":"{valor}","modificado":"{modificado}"}}\n\n'
                ultimo_valor = valor

            time.sleep(120)  # checa a cada 5 segundos
    return Response(gerar_eventos(), mimetype="text/event-stream")

@app.route("/painel-prod")
def painel_prod():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/")
def index():
    return redirect("/painel-prod")

if __name__ == "__main__":
    app.run(debug=True)
