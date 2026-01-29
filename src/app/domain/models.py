from sqlalchemy import \
    Column, Integer, String, Numeric, Date, BigInteger
from ..application.config.database import Base


class CotacaoModel(Base):
    __tablename__ = "cotacoes"

    id = Column(Integer, primary_key=True, index=True)
    data_pregrao = Column(Date, nullable=False)
    cod_bdi = Column(String(2), nullable=False)
    cod_negociacao = Column(String(12), nullable=False)
    tipo_mercado = Column(Integer, nullable=False)
    nome_resumido = Column(String(12), nullable=False)
    especificacao_papel = Column(String(10), nullable=False)
    prazo_em_dias = Column(String(3), nullable=False)
    moeda_ref = Column(String(4), nullable=False)
    preco_abertura_pregao = Column(Numeric(11,2), nullable=False)
    preco_maximo_pregao = Column(Numeric(11,2), nullable=False)
    preco_minimo_pregao = Column(Numeric(11,2), nullable=False)
    preco_medio_pregao = Column(Numeric(11,2), nullable=False)
    preco_ultimo_negociacao_pregao = Column(Numeric(11,2), nullable=False)
    preco_melhor_oferta_compra = Column(Numeric(11,2), nullable=False)
    preco_melhor_oferta_venda = Column(Numeric(11,2), nullable=False)
    total_negocios_pregao = Column(Integer, nullable=False)
    quantidade_total_titulos_negociados = Column(BigInteger, nullable=False)
    volume_total_titulos_negociados = Column(Numeric(16,2), nullable=False)
    preco_exercicio = Column(Numeric(11,2), nullable=False)
    indicador_correcao_preco_exercicio = Column(Integer, nullable=False)
    data_vencimento = Column(Date, nullable=False)
    fator_cotacao = Column(Integer, nullable=False)
    preco_exercicio_opcao_ref_dolar = Column(Numeric(13,6), nullable=False)
    codigo_isin = Column(String(12), nullable=False)
    distribuicao_papel = Column(Integer, nullable=False)