from pydantic import BaseModel, Field, field_validator
from typing import List
from enum import Enum

class Ruolo(Enum):
    #ruoli degli utenti
    admin = "admin"
    user = "user"

class Utente(BaseModel):
    #modello per la gestione degli utenti
    username: str = Field(..., min_length=1)
    password: str = Field(..., min_length=1)

        
class Macchinari(BaseModel):
    #modello per la gestione dei macchinari
    #plant_id: str
    name: str
    type: str
    status: str

class Impianti(BaseModel):
    #modello per la gestione degli impianti
    name: str
    location: str
    description: str
    machinery: List[Macchinari] = []
