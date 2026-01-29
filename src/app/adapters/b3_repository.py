from sqlalchemy import select
from ..domain.ports import B3RepositoryPort
from ..domain.models import CotacaoModel


class B3Repository(B3RepositoryPort):

    def __init__(self, session):
        self.session = session

    def obter_ativos(self, limit: int, offset: int) -> list[str]:
        # Lógica para obter ativos do repositório
        query = (
            select(CotacaoModel.cod_negociacao)
                .distinct()
                .order_by(CotacaoModel.cod_negociacao)
                .limit(limit)
                .offset(offset)
        )
        result = self.session.execute(query).yield_per(1000)
        return [row[0] for row in result.fetchall()]

    def obter_dados_historicos(self, ativo: str) -> list[CotacaoModel]:
        # Lógica para obter dados históricos de um ativo específico
        query = select(CotacaoModel).where(CotacaoModel.cod_negociacao == ativo).order_by(CotacaoModel.data_pregrao)

        result = self.session.execute(query).yield_per(1000)
        # Return ORM model instances instead of Row objects
        return result.scalars().all()