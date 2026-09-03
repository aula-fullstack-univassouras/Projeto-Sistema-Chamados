from pydantic import BaseModel
from typing import Optional


class Chamado(BaseModel):
    id: Optional[int] = None
    titulo: str
    descricao: str
    status: str = "aberto"