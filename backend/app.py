import os
from flask import Flask
from routes.api import api_dados
from routes.panel import painel_prod, index
from routes.stream import stream

app = Flask(__name__, static_folder="../frontend", static_url_path="")

# Rotas
app.route("/api/dados", methods=["GET"])(api_dados)
app.route("/painel-prod")(painel_prod)
app.route("/")(index)
app.route("/stream")(stream)

if __name__ == "__main__":
    app.run(debug=True)