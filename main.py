import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

from app import app

if __name__ == "__main__":
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
   
    print("Iniciando Sistema de Cadastro de Pessoas v2.0.0")
    print("Acesse http://localhost:5000 no seu navegador")
    app.run(debug=True, host="0.0.0.0", port=5000)