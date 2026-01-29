from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool


DATABASE_URL = "mysql+pymysql://root:ntt_projeto@localhost:3307/ntt_projeto"

engine = create_engine(
    DATABASE_URL,
    echo=False,  # desabilitar em produção para melhor performance
    poolclass=QueuePool,
    pool_size=10,
    max_overflow=20
)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()