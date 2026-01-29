from ..application.schemas.cotacao_schema import CotacaoSchema
from ..application.schemas.estatistica_schema import EstatisticaSchema
from .models import CotacaoModel

class B3Service:

    def __init__(self, repository):
        self.repository = repository

    def obter_ativos(self, limit, offset) -> list[str]:
        return self.repository.obter_ativos(limit, offset)

    def _model_to_schema(self, model: CotacaoModel) -> CotacaoSchema:
        """Converte uma instância de CotacaoModel para CotacaoSchema usando orm_mode."""
        return CotacaoSchema.from_orm(model)

    def obter_dados_historicos(self, ativo: str) -> list[CotacaoSchema]:
        models = self.repository.obter_dados_historicos(ativo)
        return [self._model_to_schema(m) for m in models]

    def estatisticas_ativo(self, ativo: str) -> EstatisticaSchema:
        dados = self.repository.obter_dados_historicos(ativo)
        if not dados:
            return None

        estatistica = EstatisticaSchema()
        return estatistica