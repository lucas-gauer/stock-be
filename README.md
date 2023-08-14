# Stock - Back end

## Setup

### Dependências

É recomendado utilizar um ambiente virtual (venv).

`pip install -r requirements.txt`

### Banco de dados

Testado utilizando o banco de dados MariaDB.
No console do banco de dados inserir
`source <path/to/file>/init_db.sql`

Neste mesmo arquivo podem ser encontradas as declarações das tabelas do banco de dados.

## Execução

`uvicorn main:app`

## Rotas

Por padrão, as rotas estão listadas e ligeiramente documentadas no endpoint /docs.

### Auth

POST /auth/login

body: name (str), password (str)

### User

POST /user

body: name (str), password (str)

### Product

As rotas de produtos estão protegidas e necessitam de um token válido.
A rota de login gera o token.
O token deve ser enviado no cabeçalho "Authorization" precedido por "Bearer "

GET /product

GET /product/{id}

POST /product - body `CreateProduct` model

PUT /product/{id} - body `CreateProduct` model

DELETE /product/{id}
