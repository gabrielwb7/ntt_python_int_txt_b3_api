from .config.database import SessionLocal
from ..domain.services import B3Service
from ..adapters.b3_repository import B3Repository

repository = B3Repository(SessionLocal())
service = B3Service(repository)

class ConsultarAtivos:

    def executar(self) -> list[str]:
        # Lógica para consultar os ativos disponíveis
        ativos = service.obter_ativos()
        return ativos