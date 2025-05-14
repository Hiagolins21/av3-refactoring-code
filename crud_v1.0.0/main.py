# meu primeiro programa de banco de dados pessoa v1.0
# autor: iniciante em python
# data: hoje
# esse programa é um crud simples que guarda pessoas em um arquivo txt

import flask
from flask import request, jsonify, render_template
import os
import json

# configuracao do app
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# arquivo pra dados
arquivo_dados = "pessoas.txt"

# inicializa o arquivo caso nao exista
def iniciar_banco():
    """funcao q inicia o banco"""
    if not os.path.exists(arquivo_dados):
        with open(arquivo_dados, "w") as f:
            f.write("[]")  # inicia com lista vazia em json

# função que pega tds as pessoas
def pegar_dados():
    """funçao q pega todos dados"""
    with open(arquivo_dados, "r") as f:
        dados = json.load(f)
    return dados

# função pra salvar
def salvar_dados(dados):
    """funcao q salva todos os dados"""
    with open(arquivo_dados, "w") as f:
        json.dump(dados, f)

# pegar o maior id
def pegar_max_id(pessoas):
    """função q pega maior id da lista"""
    if not pessoas:
        return 0
    return max(pessoa["id"] for pessoa in pessoas)

# rota principal
@app.route("/", methods=["GET"])
def pag_principal():
    """funcao da pagina principal"""
    return render_template("index.html")

# api para listar todas
@app.route("/api/pessoas", methods=["GET"])
def api_todas():
    """api q lista tudo"""
    return jsonify(pegar_dados())

# api pra pegar uma pessoa
@app.route("/api/pessoas/<int:id>", methods=["GET"])
def api_um(id):
    """api q pega 1 pessoa pelo id"""
    pessoas = pegar_dados()
    for p in pessoas:
        if p["id"] == id:
            return jsonify(p)
    return jsonify({"erro": "não achei essa pessoa!!!"})

# api para criar pessoa
@app.route("/api/pessoas", methods=["POST"])
def api_criar():
    """api q cria 1 pessoa"""
    dados = request.get_json()
    
    # validar dados
    if not "nome" in dados or not "idade" in dados or not "email" in dados:
        return jsonify({"erro": "dados incompletos!!!"})
    
    pessoas = pegar_dados()
    novo_id = pegar_max_id(pessoas) + 1
    
    nova_p = {
        "id": novo_id,
        "nome": dados["nome"],
        "idade": dados["idade"],
        "email": dados["email"]
    }
    
    pessoas.append(nova_p)
    salvar_dados(pessoas)
    
    return jsonify(nova_p)

# api para atualizar
@app.route("/api/pessoas/<int:id>", methods=["PUT"])
def api_atualiza(id):
    """api q atualiza 1 pessoa"""
    dados = request.get_json()
    
    # validar dados
    if not "nome" in dados or not "idade" in dados or not "email" in dados:
        return jsonify({"erro": "dados incompletos!!!"})
    
    pessoas = pegar_dados()
    for i, p in enumerate(pessoas):
        if p["id"] == id:
            pessoas[i] = {
                "id": id,
                "nome": dados["nome"],
                "idade": dados["idade"],
                "email": dados["email"]
            }
            salvar_dados(pessoas)
            return jsonify(pessoas[i])
    
    return jsonify({"erro": "não achei essa pessoa!!!"})

# api para deletar
@app.route("/api/pessoas/<int:id>", methods=["DELETE"])
def api_deletar(id):
    """api q deleta 1 pessoa"""
    pessoas = pegar_dados()
    for i, p in enumerate(pessoas):
        if p["id"] == id:
            del pessoas[i]
            salvar_dados(pessoas)
            return jsonify({"sucesso": "pessoa removida!!!"})
    
    return jsonify({"erro": "não achei essa pessoa!!!"})

# servir arquivos estaticos
@app.route("/<path:caminho>")
def pegar_arquivo(caminho):
    """função q pega arquivos"""
    return flask.send_from_directory(".", caminho)

# iniciar o programa
if __name__ == "__main__":
    iniciar_banco()
    app.run(host="0.0.0.0", port=5000) 