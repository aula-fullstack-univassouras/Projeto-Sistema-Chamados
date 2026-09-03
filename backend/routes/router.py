from fastapi import APIRouter

from models.chamado import Chamado

from controllers.controller import (
    get_chamados,
    get_chamado,
    post_chamado,
    put_chamado,
    delete_chamado
)


router = APIRouter()


@router.get("/chamados")
def listar():
    return get_chamados()


@router.get("/chamados/{chamado_id}")
def buscar(chamado_id: int):
    return get_chamado(chamado_id)


@router.post("/chamados")
def criar(chamado: Chamado):
    return post_chamado(chamado)


@router.put("/chamados/{chamado_id}")
def atualizar(chamado_id: int, chamado: Chamado):
    return put_chamado(chamado_id, chamado)


@router.delete("/chamados/{chamado_id}")
def excluir(chamado_id: int):
    return delete_chamado(chamado_id)