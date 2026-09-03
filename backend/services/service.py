from data.chamados import chamados


def listar_chamados():
    return chamados


def buscar_chamado(chamado_id: int):
    for chamado in chamados:
        if chamado["id"] == chamado_id:
            return chamado

    return None


def criar_chamado(titulo: str, descricao: str):
    novo_id = max([c["id"] for c in chamados], default=0) + 1

    novo_chamado = {
        "id": novo_id,
        "titulo": titulo,
        "descricao": descricao,
        "status": "aberto"
    }

    chamados.append(novo_chamado)

    return novo_chamado


def atualizar_chamado(
    chamado_id: int,
    titulo: str,
    descricao: str,
    status: str
):
    chamado = buscar_chamado(chamado_id)

    if chamado is None:
        return None

    chamado["titulo"] = titulo
    chamado["descricao"] = descricao
    chamado["status"] = status

    return chamado


def excluir_chamado(chamado_id: int):
    chamado = buscar_chamado(chamado_id)

    if chamado is None:
        return False

    chamados.remove(chamado)

    return True