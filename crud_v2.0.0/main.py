"""
Sistema de Cadastro de Pessoas v2.0.0
Arquivo principal para execução do projeto
"""
import os
import sys

# Adiciona o diretório backend ao path
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

# Importa o app do backend
from app import app

if __name__ == "__main__":
    # Verificando se o diretório de dados existe
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    # Inicializando servidor
    print("Iniciando Sistema de Cadastro de Pessoas v2.0.0")
    print("Acesse http://localhost:5000 no seu navegador")
    app.run(debug=True, host="0.0.0.0", port=5000) 