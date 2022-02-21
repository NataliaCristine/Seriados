# Seriados

O Seriados é ums sistema para armazenar e catalogar suas séries preferidas.

## Como instalar e rodar

Para instalarmos é necessário seguir alguns passos, como baixr o projeto e fazer a instalação das dependências.
Necessário abrir uma aba do terminal e digitar o seguinte:

### Este passo é para baixar o projeto:

cd git clone git@github.com:NataliaCristine/Seriados.git

### Depois que terminar de baixar o projeto entre na pasta:

cd Seriados

### Criar um ambiente virtual:

python -m venv venv

### Entrar no ambiente virtual:

source/venv/bin/activate

### Então para instalar as dependências do projeto:

pip install -r requirements.txt

### Já tendo um banco de dados criados, copie a pasta .env.example e coloque suas credenciais e nome do banco criado

### Rode as migrações:

flask db upgrade

## Utilizando o banco:

Rode o comando flask run:

Para utilizar o sistema necessário um cliente API.

Rota post

POST /seriado

Esta Rota faz a criação do seriado:

Request body:

{
"serie":"Friends",
"seasons":10,
"released_date":"06/02/1996",
"genre":"Comédia, romance",
"imdb_rating":8.8
}

RESPONSE STATUS -> HTTP 201 (created)
{
"id":1,
"serie":"Friends",
"seasons":10,
"released_date":"06/02/1996",
"genre":"Comédia, romance",
"imdb_rating":8.8
}

GET /seriado
Esta rota retorna todos os seriados cadastrados.

RESPONSE STATUS -> HTTP 200 (ok)
[{
"id":1,
"serie":"Friends",
"seasons":10,
"released_date":"06/02/1996",
"genre":"Comédia, romance",
"imdb_rating":8.8
}]

PATCH /seriado/serie_id
Esta rota é para atualizar qualquer dado da serie.

Request body:
{
"serie":"Friends",
"seasons":10,
"released_date":"06/02/1996",
"genre":"Comédia, romance",
"imdb_rating":8.8
}

RESPONSE STATUS -> HTTP 200 (ok)
{
"id":1,
"serie":"Friends",
"seasons":10,
"released_date":"06/02/1996",
"genre":"Comédia, romance",
"imdb_rating":8.8
}

DELETE /seriado/seriad_id
Esta rota deleta um seriado cadastrado.
RESPONSE STATUS -> HTTP 204 (ok)

Tecnologias utilizadas:
Django
ORM / SQLAlchemy
