from typing import List
from fastapi import APIRouter
from ..application.consultar_ativos_usecase import ConsultarAtivos

router = APIRouter()

consultar_ativos_uc = ConsultarAtivos()

@router.get("/ativos", response_model=List[str])
def get_ativos() -> List[str]:
    """Retorna uma lista de ativos disponíveis na B3."""
    return consultar_ativos_uc.executar()