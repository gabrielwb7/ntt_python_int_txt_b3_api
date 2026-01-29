from typing import List, Dict
from fastapi import APIRouter, Query
from ..application.consultar_ativos_usecase import ConsultarAtivos
from ..application.schemas.cotacao_schema import CotacaoSchema


router = APIRouter()

consultar_ativos_uc = ConsultarAtivos()


@router.get("/ativos", response_model=List[str])
def get_ativos() -> List[str]:
    """Retorna uma lista de ativos disponíveis na B3."""
    return consultar_ativos_uc.todos_ativos()


@router.get("/ativos/{ativo}", response_model=List[CotacaoSchema])
def get_dados_historicos(ativo: str) -> List[CotacaoSchema]:
    """Retorna dados historicos de um ativo específico na B3."""
    return consultar_ativos_uc.dados_historicos_ativo(ativo)


@router.get("/ativos/{ativo}/estatisticas", response_model=Dict)
def get_estatisticas_ativo(ativo: str) -> Dict:
    """Retorna dados estatísticos de um ativo específico na B3."""
    return consultar_ativos_uc.estatisticas_ativo(ativo)


@router.get("/ativos/{ativo}/grafico")
def get_grafico(
        ativo: str,
        campo: str = "preco_medio_pregao",
        comparar_ativo: bool = Query(False, description="Indica se deve comparar com outro ativo"),
        outro_ativo: str = Query(None, description="Outro ativo para comparar"),
    ):
    """Retorna dados estatísticos de um ativo específico na B3."""
    return consultar_ativos_uc.gerar_grafico(ativo, campo, comparar_ativo, outro_ativo)