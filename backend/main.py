from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi import Request

from backend.router import router
from backend.services.service import iniciar_banco


app = FastAPI(
    title="API de Chamados",
    description="Sistema simples de chamados de suporte",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.exception_handler(RequestValidationError)
async def erro_validacao(
    request: Request,
    exc: RequestValidationError
):
    return JSONResponse(
        status_code=400,
        content={
            "erro": "Dados inválidos",
            "detalhes": exc.errors()
        }
    )


app.include_router(router)


@app.on_event("startup")
def iniciar():
    iniciar_banco()


@app.get("/")
def inicio():
    return {
        "mensagem": "API de Chamados funcionando!"
    }


@app.get("/status")
def status():
    return {
        "sistema": "online",
        "banco": "SQLite",
        "api": "FastAPI"
    }


@app.get("/info")
def informacoes():
    return {
        "nome": "Projeto Chamados",
        "versao": "1.0.0",
        "documentacao": "/docs"
    }