import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))

import os
import tempfile
import pytest
from database import Database

@pytest.fixture
def db_temp():
    # Cria um arquivo temporário para o banco de dados e inicializa com []
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(b'[]')
        tmp.flush()
        db = Database(database_file=tmp.name)
        yield db
    os.remove(tmp.name)

def test_add_and_get_record(db_temp):
    pessoa = {"nome": "João", "idade": 30, "email": "joao@email.com"}
    nova = db_temp.add_record(pessoa)
    assert nova["id"] == 1
    assert nova["nome"] == "João"
    # Buscar pelo id
    buscada = db_temp.get_record_by_id(1)
    assert buscada["email"] == "joao@email.com"

def test_get_all_records(db_temp):
    assert db_temp.get_all_records() == []
    db_temp.add_record({"nome": "A", "idade": 20, "email": "a@a.com"})
    db_temp.add_record({"nome": "B", "idade": 22, "email": "b@b.com"})
    todos = db_temp.get_all_records()
    assert len(todos) == 2
    assert todos[1]["nome"] == "B"

def test_update_record(db_temp):
    db_temp.add_record({"nome": "C", "idade": 25, "email": "c@c.com"})
    atualizada = db_temp.update_record(1, {"nome": "Carlos", "idade": 26, "email": "carlos@c.com"})
    assert atualizada["nome"] == "Carlos"
    assert atualizada["idade"] == 26
    # Testa atualizar inexistente
    assert db_temp.update_record(99, {"nome": "X", "idade": 0, "email": "x@x.com"}) is None

def test_delete_record(db_temp):
    db_temp.add_record({"nome": "D", "idade": 40, "email": "d@d.com"})
    assert db_temp.delete_record(1) is True
    assert db_temp.get_all_records() == []
    # Testa deletar inexistente
    assert db_temp.delete_record(99) is False
