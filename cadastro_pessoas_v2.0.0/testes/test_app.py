import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))

import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_all_people(client):
    resp = client.get('/api/pessoas')
    assert resp.status_code == 200
    assert isinstance(resp.get_json(), list)

def test_create_and_get_person(client):
    pessoa = {"nome": "Maria", "idade": 28, "email": "maria@email.com"}
    resp = client.post('/api/pessoas', json=pessoa)
    assert resp.status_code == 201
    data = resp.get_json()
    assert data["nome"] == "Maria"
    # Buscar pelo id
    resp2 = client.get(f'/api/pessoas/{data["id"]}')
    assert resp2.status_code == 200
    assert resp2.get_json()["email"] == "maria@email.com"

def test_update_person(client):
    pessoa = {"nome": "Ana", "idade": 22, "email": "ana@email.com"}
    resp = client.post('/api/pessoas', json=pessoa)
    data = resp.get_json()
    update = {"nome": "Ana Paula", "idade": 23, "email": "anapaula@email.com"}
    resp2 = client.put(f'/api/pessoas/{data["id"]}', json=update)
    assert resp2.status_code == 200
    assert resp2.get_json()["nome"] == "Ana Paula"
    # Atualizar inexistente
    resp3 = client.put('/api/pessoas/9999', json=update)
    assert resp3.status_code == 404

def test_delete_person(client):
    pessoa = {"nome": "Carlos", "idade": 35, "email": "carlos@email.com"}
    resp = client.post('/api/pessoas', json=pessoa)
    data = resp.get_json()
    resp2 = client.delete(f'/api/pessoas/{data["id"]}')
    assert resp2.status_code == 200
    # Deletar inexistente
    resp3 = client.delete('/api/pessoas/9999')
    assert resp3.status_code == 404

def test_create_person_incomplete(client):
    pessoa = {"nome": "Sem Email", "idade": 20}
    resp = client.post('/api/pessoas', json=pessoa)
    assert resp.status_code == 400
    assert "erro" in resp.get_json() 