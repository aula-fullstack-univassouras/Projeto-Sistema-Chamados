from backend.data import chamados
from backend.models.chamado import ChamadoCreate
from backend.models.chamado import ChamadoUpdate


def iniciar_banco():
    chamados.criar_tabela()


def criar_chamado(dados: ChamadoCreate):
    titulo = dados.titulo.strip()
    descricao = dados.descricao.strip()
    status = dados.status

    chamado_id = chamados.inserir(
        titulo,
        descricao,
        status
    )

    return chamados.buscar_por_id(chamado_id)


def listar_chamados():
    return chamados.listar()


def buscar_chamado(chamado_id: int):
    return chamados.buscar_por_id(chamado_id)


def atualizar_chamado(
    chamado_id: int,
    dados: ChamadoUpdate
):
    atual = chamados.buscar_por_id(chamado_id)

    if atual is None:
        return None

    titulo = dados.titulo
    descricao = dados.descricao
    status = dados.status

    if titulo is None:
        titulo = atual["titulo"]

    if descricao is None:
        descricao = atual["descricao"]

    if status is None:
        status = atual["status"]

    chamados.atualizar(
        chamado_id,
        titulo.strip(),
        descricao.strip(),
        status
    )

    return chamados.buscar_por_id(chamado_id)


def excluir_chamado(chamado_id: int):
    atual = chamados.buscar_por_id(chamado_id)

    if atual is None:
        return False

    chamados.excluir(chamado_id)

    return True


def existe_chamado(chamado_id: int):
    resultado = chamados.buscar_por_id(chamado_id)

    return resultado is not None