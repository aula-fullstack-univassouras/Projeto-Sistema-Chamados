from fastapi import HTTPException

from backend.models.chamado import ChamadoCreate
from backend.models.chamado import ChamadoUpdate

from backend.services.service import criar_chamado
from backend.services.service import listar_chamados
from backend.services.service import buscar_chamado
from backend.services.service import atualizar_chamado
from backend.services.service import excluir_chamado


def criar(dados: ChamadoCreate):
    resultado = criar_chamado(dados)

    if resultado is None:
        raise HTTPException(
            status_code=400,
            detail="Não foi possível criar o chamado"
        )

    return resultado


def listar():
    return listar_chamados()


def buscar(chamado_id: int):
    resultado = buscar_chamado(chamado_id)

    if resultado is None:
        raise HTTPException(
            status_code=404,
            detail="Chamado não encontrado"
        )

    return resultado


def atualizar(
    chamado_id: int,
    dados: ChamadoUpdate
):
    resultado = atualizar_chamado(
        chamado_id,
        dados
    )

    if resultado is None:
        raise HTTPException(
            status_code=404,
            detail="Chamado não encontrado"
        )

    return resultado


def excluir(chamado_id: int):
    resultado = excluir_chamado(chamado_id)

    if not resultado:
        raise HTTPException(
            status_code=404,
            detail="Chamado não encontrado"
        )

    return {
        "mensagem": "Chamado excluído com sucesso"
    }


def verificar_id(chamado_id: int):
    if chamado_id <= 0:
        raise HTTPException(
            status_code=400,
            detail="ID deve ser maior que zero"
        )

    return True