from typing import List
from fastapi import APIRouter, Query
from ..application.consultar_ativos_usecase import ConsultarAtivos
from ..application.schemas.cotacao_schema import CotacaoSchema

router = APIRouter()

consultar_ativos_uc = ConsultarAtivos()

@router.get("/ativos", response_model=List[str])
def get_ativos(
    limit: int = Query(100, ge=10, le=500),
    offset: int = Query(0, ge=0)
) -> List[str]:
    """Retorna uma lista de ativos disponíveis na B3."""
    return consultar_ativos_uc.todos_ativos(limit, offset)

@router.get("/ativos/{ativo}", response_model=List[CotacaoSchema])
def get_ativos(ativo: str) -> List[CotacaoSchema]:
    """Retorna dados historicos de um ativo específico na B3."""
    return consultar_ativos_uc.dados_historicos_ativo(ativo)