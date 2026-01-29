from typing import Dict
from fastapi import FastAPI
from .adapters import b3_router


MENSAGEM_HOME: str = "Bem-vindo à API de analise de dados B3"

# Criando o App
app = FastAPI()
app.include_router(b3_router.router)


@app.get("/")
def home() -> Dict[str, str]:
    global MENSAGEM_HOME
    return {"mensagem": MENSAGEM_HOME}