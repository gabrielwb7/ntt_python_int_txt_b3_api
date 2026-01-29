

class B3Service:
    
    def __init__(self, repository):
        self.repository = repository

    def obter_ativos(self):
        return self.repository.obter_ativos()