# Anime Tracker API

Projeto de estudo focado em desenvolvimento backend.

## Objetivo

Criar uma API para gerenciar animes favoritos, contendo informações como:

- título
- número de episódios
- gênero
- estúdio
- sinopse

## Tecnologias

- Python
- FastAPI
- Uvicorn

## Executar o projeto

Criar ambiente virtual:

python -m venv venv

Ativar ambiente:

venv\Scripts\activate

Instalar dependências:

pip install fastapi uvicorn

Rodar servidor:

uvicorn main:app --reload

A API ficará disponível em:

http://127.0.0.1:8000

Documentação automática:

http://127.0.0.1:8000/docs