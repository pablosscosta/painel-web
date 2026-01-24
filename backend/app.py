import os
from flask import Flask
from routes.api import api_dados
from routes.panel import painel_prod, index
from routes.stream import stream
from routes.home import home
from routes.historico import historico

app = Flask(__name__, static_folder="../frontend", static_url_path="")

# Rotas
app.route("/api/dados", methods=["GET"])(api_dados)
app.route("/painel-prod")(painel_prod)
app.route("/", methods=["GET"])(home)
app.route("/stream")(stream)
app.route("/historico")(historico)

if __name__ == "__main__":
    app.run(debug=True)