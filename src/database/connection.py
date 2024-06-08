from sqlalchemy import create_engine, Column, Integer, String, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://insight:insight@localhost/insightdb"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class CensoNomes(Base):
    __tablename__ = 'censo_nomes'
    id = Column(Integer, primary_key=True)
    nome = Column(String(255), nullable=False)
    decada = Column(String(20), nullable=False)
    frequencia = Column(Integer, nullable=False)
    sexo = Column(CHAR(1), nullable=True)  

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()