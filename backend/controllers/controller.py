from models.chamado import Chamado

from services.service import (
    listar_chamados,
    buscar_chamado,
    criar_chamado,
    atualizar_chamado,
    excluir_chamado
)


def get_chamados():
    return listar_chamados()


def get_chamado(chamado_id: int):
    chamado = buscar_chamado(chamado_id)

    if chamado is None:
        return {"erro": "Chamado não encontrado"}

    return chamado


def post_chamado(chamado: Chamado):
    return criar_chamado(
        chamado.titulo,
        chamado.descricao
    )


def put_chamado(chamado_id: int, chamado: Chamado):
    resultado = atualizar_chamado(
        chamado_id,
        chamado.titulo,
        chamado.descricao,
        chamado.status
    )

    if resultado is None:
        return {"erro": "Chamado não encontrado"}

    return resultado


def delete_chamado(chamado_id: int):
    resultado = excluir_chamado(chamado_id)

    if not resultado:
        return {"erro": "Chamado não encontrado"}

    return {
        "mensagem": "Chamado excluído com sucesso"
    }