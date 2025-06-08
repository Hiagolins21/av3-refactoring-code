class PeopleAPI {
    constructor(baseURL = '/api/pessoas') {
        this.baseURL = baseURL;
    }

    // Método para buscar todas as pessoas
    async getAllPeople() {
        try {
            const response = await fetch(this.baseURL);
            if (!response.ok) {
                throw new Error(`Erro HTTP: ${response.status}`);
            }
            return await response.json();
        } catch (error) {
            console.error('Erro ao buscar pessoas:', error);
            throw error;
        }
    }

    // Método para buscar uma pessoa pelo ID
    async getPerson(id) {
        try {
            const response = await fetch(`${this.baseURL}/${id}`);
            if (!response.ok) {
                throw new Error(`Erro HTTP: ${response.status}`);
            }
            return await response.json();
        } catch (error) {
            console.error(`Erro ao buscar pessoa #${id}:`, error);
            throw error;
        }
    }

    // Método para criar uma nova pessoa
    async createPerson(personData) {
        try {
            const response = await fetch(this.baseURL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(personData)
            });

            if (!response.ok) {
                throw new Error(`Erro HTTP: ${response.status}`);
            }

            return await response.json();
        } catch (error) {
            console.error('Erro ao criar pessoa:', error);
            throw error;
        }
    }

    // Método para atualizar uma pessoa existente
    async updatePerson(id, personData) {
        try {
            const response = await fetch(`${this.baseURL}/${id}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(personData)
            });

            if (!response.ok) {
                throw new Error(`Erro HTTP: ${response.status}`);
            }

            return await response.json();
        } catch (error) {
            console.error(`Erro ao atualizar pessoa #${id}:`, error);
            throw error;
        }
    }

    // Método para excluir uma pessoa
    async deletePerson(id) {
        try {
            const response = await fetch(`${this.baseURL}/${id}`, {
                method: 'DELETE'
            });

            if (!response.ok) {
                throw new Error(`Erro HTTP: ${response.status}`);
            }

            return await response.json();
        } catch (error) {
            console.error(`Erro ao excluir pessoa #${id}:`, error);
            throw error;
        }
    }
}

// Classe para gerenciar a UI
class PeopleUI {
    constructor(api) {
        this.api = api;
        this.isEditing = false;

        // DOM
        this.form = document.getElementById('personForm');
        this.personIdInput = document.getElementById('personId');
        this.nameInput = document.getElementById('name');
        this.ageInput = document.getElementById('age');
        this.emailInput = document.getElementById('email');
        this.peopleTable = document.getElementById('peopleTable');
        this.formTitle = document.getElementById('formTitle');
        this.saveButton = document.getElementById('saveButton');
        this.cancelButton = document.getElementById('cancelButton');
        this.messageArea = document.getElementById('messageArea');

        // Inicializar eventos
        this.initEventListeners();

        // Carregar pessoas ao iniciar
        this.loadPeople();
    }

    // Configurar listeners de eventos
    initEventListeners() {
        // Evento de submit do formulário
        this.form.addEventListener('submit', (e) => {
            e.preventDefault();
            this.savePerson();
        });

        // Evento de cancelar edição
        this.cancelButton.addEventListener('click', () => {
            this.resetForm();
        });
    }

    // Carregar pessoas do servidor
    async loadPeople() {
        try {
            const people = await this.api.getAllPeople();
            this.renderPeopleTable(people);
        } catch (error) {
            this.showMessage('Erro ao carregar dados. Tente novamente mais tarde.', 'danger');
        }
    }

    // Renderizar tabela de pessoas
    renderPeopleTable(people) {
        this.peopleTable.innerHTML = '';

        if (people.length === 0) {
            const row = document.createElement('tr');
            const cell = document.createElement('td');
            cell.colSpan = 5;
            cell.textContent = 'Nenhuma pessoa cadastrada';
            cell.classList.add('text-center');
            row.appendChild(cell);
            this.peopleTable.appendChild(row);
            return;
        }

        people.forEach(person => {
            const row = document.createElement('tr');
            row.dataset.id = person.id;

            // Colunas de dados
            row.innerHTML = `
                <td>${person.id}</td>
                <td>${person.nome}</td>
                <td>${person.idade}</td>
                <td>${person.email}</td>
                <td class="action-buttons">
                    <button class="btn btn-primary btn-edit">
                        <i class="bi bi-pencil"></i> Editar
                    </button>
                    <button class="btn btn-danger btn-delete">
                        <i class="bi bi-trash"></i> Excluir
                    </button>
                </td>
            `;

            // Adicionar eventos aos botões
            const editButton = row.querySelector('.btn-edit');
            const deleteButton = row.querySelector('.btn-delete');

            editButton.addEventListener('click', () => this.editPerson(person));
            deleteButton.addEventListener('click', () => this.confirmDeletePerson(person.id));

            this.peopleTable.appendChild(row);
        });
    }

    // Salvar pessoa (criar ou atualizar)
    async savePerson() {
        const personData = {
            nome: this.nameInput.value,
            idade: parseInt(this.ageInput.value),
            email: this.emailInput.value
        };

        try {
            let result;

            if (this.isEditing) {
                const id = parseInt(this.personIdInput.value);
                result = await this.api.updatePerson(id, personData);
                this.showMessage('Pessoa atualizada com sucesso!', 'success');
            } else {
                result = await this.api.createPerson(personData);
                this.showMessage('Pessoa cadastrada com sucesso!', 'success');
            }

            this.resetForm();
            await this.loadPeople();

            // Destacar a linha adicionada/editada
            setTimeout(() => {
                const row = this.peopleTable.querySelector(`tr[data-id="${result.id}"]`);
                if (row) {
                    row.classList.add('highlight');
                }
            }, 100);

        } catch (error) {
            this.showMessage('Erro ao salvar dados. Verifique os campos e tente novamente.', 'danger');
        }
    }

    // Preparar formulário para edição
    editPerson(person) {
        this.isEditing = true;
        this.personIdInput.value = person.id;
        this.nameInput.value = person.nome;
        this.ageInput.value = person.idade;
        this.emailInput.value = person.email;

        this.formTitle.textContent = 'Editar Pessoa';
        this.saveButton.innerHTML = '<i class="bi bi-check-circle"></i> Atualizar';
        this.cancelButton.classList.remove('d-none');

        // Rolar para o formulário
        this.form.scrollIntoView({ behavior: 'smooth' });
    }

    // Confirmar exclusão de pessoa
    confirmDeletePerson(id) {
        if (confirm('Tem certeza que deseja excluir esta pessoa?')) {
            this.deletePerson(id);
        }
    }

    // Excluir pessoa
    async deletePerson(id) {
        try {
            await this.api.deletePerson(id);
            this.showMessage('Pessoa excluída com sucesso!', 'success');
            await this.loadPeople();
        } catch (error) {
            this.showMessage('Erro ao excluir pessoa. Tente novamente mais tarde.', 'danger');
        }
    }

    // Resetar formulário
    resetForm() {
        this.isEditing = false;
        this.form.reset();
        this.personIdInput.value = '';

        this.formTitle.textContent = 'Adicionar Pessoa';
        this.saveButton.innerHTML = '<i class="bi bi-save"></i> Salvar';
        this.cancelButton.classList.add('d-none');
    }

    // Exibir mensagem
    showMessage(message, type) {
        this.messageArea.textContent = message;
        this.messageArea.className = `alert alert-${type}`;

        // Mostrar a mensagem
        this.messageArea.classList.remove('d-none');

        // Esconder depois de 3 segundos
        setTimeout(() => {
            this.messageArea.classList.add('d-none');
        }, 3000);
    }
}

// Inicializar a aplicação quando o DOM estiver pronto
document.addEventListener('DOMContentLoaded', () => {
    const api = new PeopleAPI();
    const ui = new PeopleUI(api);
});