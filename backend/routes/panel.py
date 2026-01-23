from flask import send_from_directory, redirect

def painel_prod():
    return send_from_directory("../frontend", "index.html")

def index():
    return redirect("/painel-prod")