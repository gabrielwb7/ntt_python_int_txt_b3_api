from .config.database import SessionLocal
from ..domain.services import B3Service
from ..adapters.b3_repository import B3Repository
from ..application.schemas.cotacao_schema import CotacaoSchema
from ..application.schemas.estatistica_schema import EstatisticaSchema

repository = B3Repository(SessionLocal())
service = B3Service(repository)

class ConsultarAtivos:

    def todos_ativos(self, limit: int = 100, offset: int = 0) -> list[str]:
        ativos = service.obter_ativos(limit, offset)
        return ativos

    def dados_historicos_ativo(self, ativo: str) -> list[CotacaoSchema]:
        dados = service.obter_dados_historicos(ativo)
        return dados

    def estatisticas_ativo(self, ativo: str) -> EstatisticaSchema:
        dados = service.estatisticas_ativo(ativo)
        return dados