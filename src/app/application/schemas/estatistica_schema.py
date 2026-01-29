from pydantic import BaseModel

class EstatisticaSchema(BaseModel):
    media_preco: float
    mediana_preco: float
    desvio_padrao_preco: float
    minimo_preco: float
    maximo_preco: float
   