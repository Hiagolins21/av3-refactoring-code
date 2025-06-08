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