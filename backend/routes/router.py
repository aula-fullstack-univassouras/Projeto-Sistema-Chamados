from fastapi import APIRouter

from backend.models.chamado import Chamado
from backend.models.chamado import ChamadoCreate
from backend.models.chamado import ChamadoUpdate

from backend.controller import criar
from backend.controller import listar
from backend.controller import buscar
from backend.controller import atualizar
from backend.controller import excluir
from backend.controller import verificar_id


router = APIRouter(
    prefix="/chamados",
    tags=["Chamados"]
)


@router.post(
    "",
    response_model=Chamado,
    status_code=201
)
def criar_chamado(dados: ChamadoCreate):
    return criar(dados)


@router.get(
    "",
    response_model=list[Chamado]
)
def listar_chamados():
    return listar()


@router.get(
    "/{chamado_id}",
    response_model=Chamado
)
def buscar_chamado(chamado_id: int):
    verificar_id(chamado_id)
    return buscar(chamado_id)


@router.put(
    "/{chamado_id}",
    response_model=Chamado
)
def atualizar_chamado(
    chamado_id: int,
    dados: ChamadoUpdate
):
    verificar_id(chamado_id)
    return atualizar(chamado_id, dados)


@router.delete(
    "/{chamado_id}"
)
def excluir_chamado(chamado_id: int):
    verificar_id(chamado_id)
    return excluir(chamado_id)


def informacoes_rotas():
    return {
        "post": "/chamados",
        "get": "/chamados",
        "get_id": "/chamados/{id}",
        "put": "/chamados/{id}",
        "delete": "/chamados/{id}"
    }