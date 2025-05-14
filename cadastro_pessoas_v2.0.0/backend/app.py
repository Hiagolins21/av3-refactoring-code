"""
Aplicação principal da API
"""
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from database import Database

app = Flask(__name__, static_folder="../frontend")
CORS(app)  # Habilita CORS para todas as rotas

# Inicializa o banco de dados
db = Database()

@app.route("/")
def index():
    """Rota para a página principal"""
    return send_from_directory(app.static_folder, "index.html")

@app.route("/<path:path>")
def static_files(path):
    """Rota para servir arquivos estáticos"""
    return send_from_directory(app.static_folder, path)

@app.route("/api/pessoas", methods=["GET"])
def get_all_people():
    """Retorna todas as pessoas cadastradas"""
    return jsonify(db.get_all_records())

@app.route("/api/pessoas/<int:person_id>", methods=["GET"])
def get_person(person_id):
    """Retorna uma pessoa específica pelo ID"""
    person = db.get_record_by_id(person_id)
    
    if person:
        return jsonify(person)
    
    return jsonify({"erro": "Pessoa não encontrada"}), 404

@app.route("/api/pessoas", methods=["POST"])
def create_person():
    """Cria uma nova pessoa"""
    data = request.get_json()
    
    # Validação dos dados
    if not all(key in data for key in ["nome", "idade", "email"]):
        return jsonify({"erro": "Dados incompletos"}), 400
    
    # Cria o registro
    new_person = db.add_record(data)
    return jsonify(new_person), 201

@app.route("/api/pessoas/<int:person_id>", methods=["PUT"])
def update_person(person_id):
    """Atualiza uma pessoa existente"""
    data = request.get_json()
    
    # Validação dos dados
    if not all(key in data for key in ["nome", "idade", "email"]):
        return jsonify({"erro": "Dados incompletos"}), 400
    
    # Atualiza o registro
    updated_person = db.update_record(person_id, data)
    
    if updated_person:
        return jsonify(updated_person)
    
    return jsonify({"erro": "Pessoa não encontrada"}), 404

@app.route("/api/pessoas/<int:person_id>", methods=["DELETE"])
def delete_person(person_id):
    """Remove uma pessoa pelo ID"""
    success = db.delete_record(person_id)
    
    if success:
        return jsonify({"mensagem": "Pessoa removida com sucesso"})
    
    return jsonify({"erro": "Pessoa não encontrada"}), 404

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000) 