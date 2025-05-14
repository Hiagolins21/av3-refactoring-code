# Sistema de Cadastro de Pessoas v1.0.0

Este é um sistema simples de cadastro de pessoas que permite adicionar, visualizar, editar e excluir registros de pessoas através de uma interface web.

## O que o sistema faz?

- Cadastra pessoas com nome, idade e email
- Mostra lista de pessoas cadastradas
- Permite editar dados das pessoas
- Permite excluir pessoas

## Requisitos

Para usar este sistema você precisa ter:

- Python 3.6 ou mais recente
- Navegador web (Chrome, Firefox, Edge, etc.)

## Como instalar

1. Baixe os arquivos deste projeto
2. Abra o terminal ou prompt de comando
3. Navegue até a pasta do projeto
4. Instale a biblioteca Flask com o comando:

```
pip install flask
```

## Como executar

1. Abra o terminal ou prompt de comando
2. Navegue até a pasta do projeto
3. Execute o seguinte comando:

```
python main.py
```

4. Abra seu navegador e acesse o endereço: `http://localhost:5000`

## Como usar

### Para adicionar uma pessoa:

1. Preencha os campos Nome, Idade e Email
2. Clique no botão "Salvar"

### Para editar uma pessoa:

1. Na lista de pessoas, clique no botão "Editar" ao lado do registro que deseja modificar
2. Os dados serão carregados no formulário
3. Altere os dados desejados
4. Clique em "Atualizar"

### Para excluir uma pessoa:

1. Na lista de pessoas, clique no botão "Excluir" ao lado do registro que deseja remover
2. Confirme a exclusão

## Estrutura do projeto

O projeto é composto por dois arquivos principais:

- `main.py`: Contém o código do servidor em Python que gerencia os dados
- `index.html`: Contém a interface do usuário com HTML, CSS e JavaScript

Os dados são salvos em um arquivo chamado `pessoas.txt` que é criado automaticamente quando o programa é executado pela primeira vez.

## Observações

- Este é um projeto simples para fins educacionais
- Os dados são armazenados localmente em um arquivo de texto
- O sistema funciona apenas no computador onde está sendo executado 