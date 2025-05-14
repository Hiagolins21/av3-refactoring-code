# Sistema de Cadastro de Pessoas v2.0.0

Um sistema moderno de cadastro de pessoas, desenvolvido como uma aplicação web utilizando Python (Flask) no backend e HTML, CSS e JavaScript no frontend. Esta é uma versão refatorada e melhorada do projeto original.

![Sistema de Cadastro de Pessoas](https://via.placeholder.com/800x400?text=Sistema+de+Cadastro+de+Pessoas+v2.0.0)

## Características

- Interface moderna e responsiva usando Bootstrap 5
- Backend modularizado em Python com Flask
- API RESTful para operações CRUD
- Frontend desenvolvido com JavaScript moderno (classes e ES6+)
- Organização clara de código por responsabilidades
- Validação de formulários
- Experiência de usuário aprimorada com animações e feedback

## Estrutura do Projeto

```
crud_v2.0.0/
│
├── backend/              # Código do servidor
│   ├── __init__.py       # Marca o diretório como um pacote Python
│   ├── app.py            # Aplicação Flask e rotas da API
│   └── database.py       # Classe para gerenciamento do banco de dados
│
├── frontend/             # Interface do usuário
│   ├── css/
│   │   └── styles.css    # Estilos personalizados
│   ├── js/
│   │   └── app.js        # Lógica do frontend em JavaScript
│   └── index.html        # Página HTML principal
│
├── data/                 # Diretório para armazenamento de dados (criado automaticamente)
│   └── pessoas.json      # Arquivo JSON para armazenar os dados (criado automaticamente)
│
├── main.py               # Script principal para iniciar a aplicação
├── requirements.txt      # Dependências do projeto
└── README.md             # Documentação do projeto
```

## Requisitos

- Python 3.7 ou superior
- Navegador web moderno (Chrome, Firefox, Edge, etc.)
- Conexão com a internet (para carregar bibliotecas CDN)

## Instalação

### 1. Clone ou faça download do projeto

```bash
git clone https://github.com/caiquemiranda/av3-refactoring-code
cd crud_v2.0.0
```

### 2. Configuração do ambiente Python

Recomenda-se a criação de um ambiente virtual:

```bash
# Criando ambiente virtual
python -m venv venv

# Ativando o ambiente (Windows)
venv\Scripts\activate

# Ativando o ambiente (Linux/Mac)
source venv/bin/activate
```

### 3. Instalação das dependências

```bash
pip install -r requirements.txt
```

## Executando o Sistema

Execute o arquivo principal:

```bash
python main.py
```

Acesse a aplicação no navegador:
[http://localhost:5000](http://localhost:5000)

## Uso

### Cadastro de Pessoas

1. Preencha os campos Nome, Idade e Email no formulário
2. Clique no botão "Salvar"
3. O novo registro aparecerá na tabela

### Edição de Registros

1. Clique no botão "Editar" ao lado do registro que deseja modificar
2. Os dados serão carregados no formulário
3. Faça as alterações necessárias
4. Clique no botão "Atualizar"

### Exclusão de Registros

1. Clique no botão "Excluir" ao lado do registro que deseja remover
2. Confirme a ação no diálogo de confirmação

## Diferenças em Relação à v1.0.0

- Código modularizado e organizado
- Interface de usuário moderna e responsiva
- Nomes de funções e variáveis mais descritivos e claros
- Tratamento de erros mais robusto
- Melhor estrutura de arquivos e pastas
- Comentários mais significativos
- Uso de classes e programação orientada a objetos
- Melhor experiência do usuário

## Desenvolvimento

### Backend

O backend foi desenvolvido com Flask, estruturado em módulos para facilitar a manutenção:

- `app.py`: Configuração do Flask e definição das rotas da API
- `database.py`: Classe para gerenciar operações de banco de dados

### Frontend

O frontend utiliza HTML5, CSS3 e JavaScript moderno:

- Interface construída com Bootstrap 5
- Ícones da biblioteca Bootstrap Icons
- JavaScript organizado em classes (PeopleAPI e PeopleUI)
- Uso de Fetch API para comunicação com o backend
- Estilização personalizada para melhorar a experiência do usuário

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para melhorar o projeto.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes. 