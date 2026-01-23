from flask import render_template

def sobre():
    return render_template("sobre.html", titulo="Sobre o Sistema")