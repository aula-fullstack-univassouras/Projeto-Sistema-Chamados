from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

# Criação da instância FastAPI
app = FastAPI(title="API de Chamados")

# Modelo Pydantic para validação do corpo da requisição
class ChamadoEntrada(BaseModel):
    titulo: str
    descricao: str
    prioridade: str

# Dados em memória (conforme o escopo da Aula 05)
chamados = []

# Rota inicial
@app.get("/")
def inicio():
    return {"mensagem": "API de Chamados ativa"}

# Rota para listar chamados
@app.get("/chamados")
def listar_chamados():
    return chamados

# Rota para criar chamados (POST)
@app.post("/chamados", status_code=status.HTTP_201_CREATED)
def criar_chamado(dados: ChamadoEntrada):
    chamado = {
        "id": len(chamados) + 1,
        **dados.model_dump(),
        "status": "aberto"
    }
    chamados.append(chamado)
    return chamado

# Rota para buscar chamado por ID
@app.get("/chamados/{chamado_id}")
def buscar_chamado(chamado_id: int):
    for chamado in chamados:
        if chamado["id"] == chamado_id:
            return chamado
    raise HTTPException(
        status_code=404,
        detail="Chamado não encontrado"
    )

# Desafio adicional: Rota para buscar chamado por status
@app.get("/chamados/status/{status_chamado}")
def buscar_chamado_por_status(status_chamado: str):
    return [c for c in chamados if c.get("status") == status_chamado]