from sqlalchemy import select
from ..domain.ports import B3RepositoryPort
from ..domain.models import CotacaoModel


class B3Repository(B3RepositoryPort):

    def __init__(self, session):
        self.session = session

    def obter_ativos(self) -> list[str]:
        # Lógica para obter ativos do repositório
        query = select(CotacaoModel.cod_negociacao).distinct().order_by(CotacaoModel.cod_negociacao)
        result = self.session.execute(query).yield_per(1000)
        return [row[0] for row in result.fetchall()]