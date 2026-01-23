import time
from flask import Response
from file_reader import ler_arquivo
from datetime import datetime
import os
import json

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
            yield f'data: {json.dumps({"valor": valor, "modificado": modificado})}\n\n'
            ultimo_valor = valor

        time.sleep(120) 

def stream():

    return Response(gerar_eventos(), mimetype="text/event-stream")