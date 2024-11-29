from fastapi import APIRouter, status, Query, HTTPException
from modello.basemodel import Utente
from utilità.utils import user_collection

router = APIRouter()

@router.post("/login")
async def login(utente: Utente):
    db_utente = user_collection.find_one({"username": utente.username})
    if db_utente and db_utente['password'] == utente.password:
        return {"msg": "Login effettuato con successo"}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenziali non valide")