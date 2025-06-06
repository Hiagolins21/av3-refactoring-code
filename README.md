# Projeto de Refatoração - Sistema de Cadastro de Pessoas

Este repositório contém duas versões de um sistema de cadastro de pessoas, desenvolvido como parte de um exercício de refatoração. O objetivo é demonstrar a evolução de um código inicial (versão 1.0.0) para uma versão refatorada, otimizada e com maior eficiência no código (versão 2.0.0).

## Estrutura do Repositório

```
/
├── cadastro_pessoas_v1.0.0/          # Versão inicial do projeto
│   ├── main.py                       # Backend em Python (códio monolítico)
│   ├── templates/
│   │   └── index.html                # Frontend com HTML, CSS e JS em um único arquivo
│   └── README.md                     # Instruções da versão 1.0.0
│
├── cadastro_pessoas_v2.0.0/          # Versão refatorada do projeto
│   ├── backend/                      # Código do servidor modularizado
│   │   ├── __init__.py               # Inicializador do pacote Python
│   │   ├── app.py                    # Aplicação Flask e rotas da API
│   │   └── database.py               # Classe para gerenciamento do banco de dados
│   ├── frontend/                     # Interface do usuário modularizada
│   │   ├── css/
│   │   │   └── styles.css            # Estilos separados
│   │   ├── js/
│   │   │   └── app.js                # JavaScript organizado em classes
│   │   └── index.html                # HTML estruturado
│   ├── main.py                       # Script principal
│   ├── requirements.txt              # Dependências do projeto
│   └── README.md                     # Documentação detalhada
│
├── .gitignore                        # Configurações para ignorar arquivos no Git
└── README.md                         # Este arquivo
```

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
cd cadastro_pessoas_v1.0.0
pip install flask
python main.py
```

### Versão 2.0.0

```bash
cd cadastro_pessoas_v2.0.0
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
