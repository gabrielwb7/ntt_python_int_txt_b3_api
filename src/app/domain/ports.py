from abc import ABC, abstractmethod

class B3RepositoryPort(ABC):
    
    @abstractmethod
    def obter_ativos(self) -> list[str]:
        """Obtém a lista de ativos disponíveis na B3."""
        pass
