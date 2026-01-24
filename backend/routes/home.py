from flask import render_template
from datetime import datetime
import os
from config import config

def home():
    return render_template(
        "home.html",
        fabrica_nome="Indústria"
    )