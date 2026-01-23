from flask import render_template
from datetime import datetime
import os
from config import config

def home():
    return render_template(
        "home.html",
        fabrica_nome="Indústria",  # Podemos mover para config.py depois
        arquivo_monitorado=config.CSV_PATH,
        ultima_verificacao=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    )