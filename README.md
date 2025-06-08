# Sistema de Cadastro de Pessoas v2.0.0

Um sistema moderno de cadastro de pessoas, desenvolvido como uma aplicação web utilizando Python (Flask) no backend e HTML, CSS e JavaScript no frontend. Esta é uma versão refatorada e melhorada do projeto original.

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
v2.0.0/
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

# Projeto de Refatoração - Sistema de Cadastro de Pessoas

Este repositório contém duas versões de um sistema de cadastro de pessoas, desenvolvido como parte de um exercício de refatoração. O objetivo é demonstrar a evolução de um código inicial (versão 1.0.0) para uma versão refatorada e otimizada (versão 2.0.0).


## Sobre o Projeto

O Sistema de Cadastro de Pessoas é uma aplicação web para criar, visualizar, editar e excluir (CRUD) registros de pessoas. Cada pessoa possui informações como nome, idade e e-mail.

### Versão 1.0.0

A versão inicial representa um código de "nível iniciante" com várias características de código não otimizado:

- Backend em Python usando Flask em um único arquivo
- Frontend com HTML, CSS e JavaScript no mesmo arquivo
- Nomes de funções e variáveis pouco descritivos (ex: `cp()`, `s()`, `lf()`)
- Comentários excessivos e pouco úteis
- Sem separação de responsabilidades
- Estrutura desorganizada
- Armazenamento de dados em arquivo de texto simples

### Versão 2.0.0

A versão refatorada apresenta significativas melhorias:

- **Modularização**: Separação clara entre backend e frontend
- **Organização**: Arquivos divididos por responsabilidade
- **Nomenclatura**: Nomes claros e descritivos para funções e variáveis
- **Estrutura de Dados**: Armazenamento em JSON com estrutura melhorada
- **Design Moderno**: Interface responsiva usando Bootstrap 5
- **Programação Orientada a Objetos**: Uso de classes e métodos bem definidos
- **Tratamento de Erros**: Melhor gerenciamento de erros e exceções
- **Experiência do Usuário**: Feedback visual, animações e mensagens informativas

## Principais Refatorações

| Aspecto | Versão 1.0.0 | Versão 2.0.0 |
|---------|------------|------------|
| Estrutura | Monolítica | Modular |
| Arquivos | 2 arquivos com todo o código | 7+ arquivos organizados |
| Nomes | Abreviados (ex: `s()`, `d()`) | Descritivos (ex: `savePerson()`, `deletePerson()`) |
| Classes | Nenhuma | Múltiplas com responsabilidades bem definidas |
| UI | Básica | Moderna e responsiva |
| Comentários | Excessivos e redundantes | Significativos e em docstrings |
| Dados | Arquivo texto | JSON estruturado |
| Erros | Tratamento mínimo | Robusto com feedback |

## Como Executar

### Versão 1.0.0

```bash
git checkout 
pip install flask
python main.py
```

### Versão 2.0.0

```bash
git main
pip install -r requirements.txt
python main.py
```

Ambas as versões iniciam um servidor web na porta 5000, acessível em http://localhost:5000

## Objetivo Educacional

Este projeto serve como exemplo didático de refatoração, demonstrando:

1. Como código mal estruturado pode evoluir para código bem organizado
2. A importância de nomear variáveis e funções adequadamente
3. Os benefícios da modularização e separação de responsabilidades
4. Como melhorar a experiência do usuário sem alterar a funcionalidade base
5. Boas práticas de programação em Python e JavaScript

## Autor

Este projeto foi criado como parte de um trabalho acadêmico sobre refatoração de código.
