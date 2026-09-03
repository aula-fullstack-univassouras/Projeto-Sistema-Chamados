from fastapi import FastAPI
from routes.router import router


app = FastAPI(
    title="API de Chamados",
    description="API para gerenciamento de chamados",
    version="1.0.0"
)


app.include_router(router)


@app.get("/")
def inicio():
    return {
        "mensagem": "API de Chamados funcionando!"
    }