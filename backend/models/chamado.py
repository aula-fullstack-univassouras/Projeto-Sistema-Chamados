from pydantic import BaseModel, Field
from typing import Literal, Optional


class ChamadoBase(BaseModel):
    titulo: str = Field(..., min_length=3, max_length=120)
    descricao: str = Field(..., min_length=3)
    status: Literal["aberto", "em_andamento", "fechado"] = "aberto"


class ChamadoCreate(ChamadoBase):
    pass


class ChamadoUpdate(BaseModel):
    titulo: Optional[str] = Field(None, min_length=3, max_length=120)
    descricao: Optional[str] = Field(None, min_length=3)
    status: Optional[
        Literal["aberto", "em_andamento", "fechado"]
    ] = None


class Chamado(ChamadoBase):
    id: int
    criado_em: str

    class Config:
        from_attributes = True


def validar_status(status: str) -> bool:
    status_permitidos = [
        "aberto",
        "em_andamento",
        "fechado"
    ]

    return status in status_permitidos


def criar_chamado_exemplo() -> ChamadoCreate:
    return ChamadoCreate(
        titulo="Exemplo",
        descricao="Chamado de exemplo",
        status="aberto"
    )


def verificar_titulo(titulo: str) -> bool:
    if titulo is None:
        return False

    if len(titulo.strip()) < 3:
        return False

    return True


def verificar_descricao(descricao: str) -> bool:
    if descricao is None:
        return False

    if len(descricao.strip()) < 3:
        return False

    return True