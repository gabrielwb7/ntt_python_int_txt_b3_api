import pandas as pd
from ..application.schemas.cotacao_schema import CotacaoSchema
from .models import CotacaoModel


class B3Service:

    def __init__(self, repository):
        self.repository = repository

    def obter_ativos(self) -> list[str]:
        return self.repository.obter_ativos()

    def _model_to_schema(self, model: CotacaoModel) -> CotacaoSchema:
        """Converte uma instância de CotacaoModel para CotacaoSchema usando orm_mode."""
        return CotacaoSchema.from_orm(model)

    def obter_dados_historicos(self, ativo: str) -> list[CotacaoSchema]:
        models = self.repository.obter_dados_historicos(ativo)
        return [self._model_to_schema(m) for m in models]

    def obter_dados_historicos_dataframe(self, ativo: str):
        """Retorna os dados históricos de um ativo como um DataFrame."""
        dados = self.repository.obter_dados_historicos(ativo)
        if not dados:
            return None
        
        return pd.DataFrame([{
            "data_pregrao": d.data_pregrao,
            "cod_negociacao": d.cod_negociacao,
            "preco_abertura_pregao": float(d.preco_abertura_pregao),
            "preco_maximo_pregao": float(d.preco_maximo_pregao),
            "preco_minimo_pregao": float(d.preco_minimo_pregao),
            "preco_medio_pregao": float(d.preco_medio_pregao),
            "preco_ultimo_negociacao_pregao": float(d.preco_ultimo_negociacao_pregao),
            "volume_total_titulos_negociados": float(d.volume_total_titulos_negociados),
        } for d in dados])


    def obter_dados_historicos_de_dois_ativos(self, ativo: str, outro_ativo: str):
        """Retorna os dados históricos de dois ativos como um DataFrame."""
        dados = self.repository.obter_dados_historicos_de_dois_ativos(ativo, outro_ativo)
        
        if not dados:
            return None
        
        return pd.DataFrame([{
            "data_pregrao": d.data_pregrao,
            "cod_negociacao": d.cod_negociacao,
            "preco_abertura_pregao": float(d.preco_abertura_pregao),
            "preco_maximo_pregao": float(d.preco_maximo_pregao),
            "preco_minimo_pregao": float(d.preco_minimo_pregao),
            "preco_medio_pregao": float(d.preco_medio_pregao),
            "preco_ultimo_negociacao_pregao": float(d.preco_ultimo_negociacao_pregao),
            "volume_total_titulos_negociados": float(d.volume_total_titulos_negociados),
        } for d in dados])