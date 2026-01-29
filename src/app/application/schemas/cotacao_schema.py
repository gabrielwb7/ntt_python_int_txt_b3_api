from datetime import date
from pydantic import BaseModel


class CotacaoSchema(BaseModel):
    id: int
    data_pregrao: date
    cod_bdi: str
    cod_negociacao: str
    tipo_mercado: int
    nome_resumido: str
    especificacao_papel: str
    prazo_em_dias: str
    moeda_ref: str
    preco_abertura_pregao: float
    preco_maximo_pregao: float
    preco_minimo_pregao: float
    preco_medio_pregao: float
    preco_ultimo_negociacao_pregao: float
    preco_melhor_oferta_compra: float
    preco_melhor_oferta_venda: float
    total_negocios_pregao: int
    quantidade_total_titulos_negociados: int
    volume_total_titulos_negociados: float
    preco_exercicio: float
    indicador_correcao_preco_exercicio: int
    data_vencimento: date
    fator_cotacao: int
    preco_exercicio_opcao_ref_dolar: float
    codigo_isin: str
    distribuicao_papel: int

    class Config:
        from_attributes = True
        orm_mode = True
