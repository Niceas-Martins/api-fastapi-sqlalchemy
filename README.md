# api-fastapi-sqlalchemy

## Especificações 
Linguagem: Python 3.13.1

Framework: FastAPI

ORM: SQLAlchemy (Versão 2.0 ou superior recomendada para Python 3.13)

Driver do Banco: pymysql

Banco de Dados: MySQL

## 📦 Dependências
Para que o projeto funcione, você precisa instalar as seguintes bibliotecas. Crie um arquivo chamado requirements.txt na pasta api_python com este conteúdo:

Plaintext

fastapi
uvicorn
sqlalchemy
pymysql
🚀 Como Rodar o Projeto
Siga estes passos para configurar e executar a API localmente:

1. Ativar o Ambiente Virtual (venv)
É importante usar o ambiente virtual que já existe na sua pasta. No terminal, dentro da pasta api_python, execute:

PowerShell

.\venv\Scripts\activate

2. Instalar as Dependências
Com o ambiente ativado, instale as bibliotecas necessárias:

Bash

pip install -r requirements.txt

3. Configurar o Banco de Dados
Certifique-se de que seu MySQL está rodando e que existe um banco de dados chamado seubanco.

Nota: Se necessário, ajuste o usuário e a senha no arquivo database.py.

4. Executar a API
Inicie o servidor utilizando o Uvicorn:

Bash

uvicorn main:app --reload

5. Acessar a Documentação
Acesse o navegador no endereço:

Swagger UI: http://127.0.0.1:8000/docs

## 💡 Sobre a Implementação do ORM
O projeto utiliza SQLAlchemy para mapear as classes Python para tabelas do banco de dados:

database.py: Gerencia a engine de conexão e a criação da sessão (SessionLocal).

models.py: Define a estrutura das tabelas como classes Python.

main.py: Contém os endpoints da API que utilizam a sessão do banco para realizar operações de CRUD.

