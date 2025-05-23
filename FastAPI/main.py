"""
Primeira coisa a fazer é criar um ambiente virtual com o comando:

- python -m venv nome_da_venv

Depois tem que ativar com o comando:

- venv\Scripts\Activate 

para depois começar a instalar o FASTPI e UVICORN com os comandos:

- pip install fastapi
- pip install uvicorn

depois disso terá que criar o código e digitar o comando:

- uvicorn main(nome do arquivo python):app (nome da variavel do FastAPI) --reload

Ex: uvicorn main:app --reload
"""

from fastapi import FastAPI

app = FastAPI()

vendas = {
    1: {'item': 'lata', "preco_unitario": 4, "quantidade": 5},
    2: {'item': 'garrafa 2L', "preco_unitario": 15, "quantidade": 2},
    3: {'item': 'garrafa 750ml', "preco_unitario": 10, "quantidade": 3},
    4: {'item': 'lata mini', "preco_unitario": 2, "quantidade": 1},
}

@app.get("/")
def home():
    return {"Vendas": len(vendas)}

@app.get("/vendas/{id_venda}")
def pegar_venda(id_venda: int):
    if id_venda in vendas:
        return vendas[id_venda]
    else:
        return {"Error": "ID inexistente"}
    