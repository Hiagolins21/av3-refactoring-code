from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from database import Database


app = Flask(__name__, static_folder="../frontend")
CORS(app)  # CORS para todas as rotas

db = Database()

@app.route("/")
def index():
    """Rota para a página principal"""
    return send_from_directory(app.static_folder, "index.html")


@app.route("/<path:path>")
def static_files(path):
    """Rota para servir arquivos estáticos"""
    return send_from_directory(app.static_folder, path)


