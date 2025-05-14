"""
Módulo de gerenciamento de banco de dados
"""
import os
import json

class Database:
    """Classe para gerenciar operações do banco de dados"""
    
    def __init__(self, database_file="data/pessoas.json"):
        """Inicializa o banco de dados"""
        self.database_file = database_file
        self._ensure_data_directory()
    
    def _ensure_data_directory(self):
        """Garante que o diretório de dados existe"""
        data_dir = os.path.dirname(self.database_file)
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        
        # Inicializa o arquivo se não existir
        if not os.path.exists(self.database_file):
            with open(self.database_file, "w", encoding="utf-8") as file:
                json.dump([], file)
    
    def get_all_records(self):
        """Retorna todos os registros do banco de dados"""
        with open(self.database_file, "r", encoding="utf-8") as file:
            return json.load(file)
    
    def save_records(self, records):
        """Salva os registros no banco de dados"""
        with open(self.database_file, "w", encoding="utf-8") as file:
            json.dump(records, file, indent=2)
    
    def get_record_by_id(self, record_id):
        """Busca um registro pelo ID"""
        records = self.get_all_records()
        for record in records:
            if record["id"] == record_id:
                return record
        return None
    
    def add_record(self, record_data):
        """Adiciona um novo registro"""
        records = self.get_all_records()
        
        # Gera um novo ID
        new_id = self._get_next_id(records)
        
        # Cria o novo registro
        new_record = {
            "id": new_id,
            "nome": record_data["nome"],
            "idade": record_data["idade"],
            "email": record_data["email"]
        }
        
        # Adiciona à lista e salva
        records.append(new_record)
        self.save_records(records)
        
        return new_record
    
    def update_record(self, record_id, record_data):
        """Atualiza um registro existente"""
        records = self.get_all_records()
        
        for i, record in enumerate(records):
            if record["id"] == record_id:
                records[i] = {
                    "id": record_id,
                    "nome": record_data["nome"],
                    "idade": record_data["idade"],
                    "email": record_data["email"]
                }
                self.save_records(records)
                return records[i]
        
        return None
    
    def delete_record(self, record_id):
        """Remove um registro pelo ID"""
        records = self.get_all_records()
        
        for i, record in enumerate(records):
            if record["id"] == record_id:
                del records[i]
                self.save_records(records)
                return True
        
        return False
    
    def _get_next_id(self, records):
        """Gera o próximo ID disponível"""
        if not records:
            return 1
        return max(record["id"] for record in records) + 1 