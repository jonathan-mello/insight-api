from fastapi import APIRouter, Depends, HTTPException
from src.database.connection import get_db, CensoNomes
from sqlalchemy.orm import Session
import requests
from typing import Optional

router = APIRouter()

@router.get("/")
def read_root(db: Session = Depends(get_db)):
    return {"message": "Hello World with Database"}

@router.post("/censo/nome")
def create_censo_nome(req: dict, db: Session = Depends(get_db)):
    nome = req.get("nome")
    sexo = req.get("sexo").upper()
    
    if not nome or not sexo:
        raise HTTPException(status_code=400, detail="Nome e sexo são obrigatórios.")
    
    url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}?sexo={sexo}"
    response = requests.get(url)
    data = response.json()
    
    for item in data:
        for res in item["res"]:
            periodo = res["periodo"]
            decada_formatada = periodo[1:5]
            if "[" in decada_formatada:
                decada_formatada = 1920
            frequencia = res["frequencia"]
            
            novo_censo = CensoNomes(
                nome = item["nome"],
                decada = decada_formatada,
                frequencia = frequencia,
                sexo = item["sexo"]
            )
            
            db.add(novo_censo)
    db.commit()
    return {"message": "Dados inseridos com sucesso"}

@router.get("/nomes")
def get_nomes(sexo: Optional[str]=None, decada: Optional[str]=None, nome: Optional[str]=None, db: Session = Depends(get_db)):
    query = db.query(CensoNomes)
    
    if nome:
        query = query.filter(CensoNomes.nome == nome.upper())
    if sexo:
        query = query.filter(CensoNomes.sexo == sexo.upper())
    if decada:
        query = query.filter(CensoNomes.decada == decada)
    
    results = query.all()
    return results