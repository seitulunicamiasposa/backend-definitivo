from fastapi import APIRouter, status, HTTPException
from modello.basemodel import Impianti
from utilità.utils import plant_collection
from bson.objectid import ObjectId
from utilità.utils import toString

router = APIRouter()

@router.get("/impianti")
async def get_plants():
    impianti = list(plant_collection.find())
    for impianto in impianti:
        impianto["_id"] = toString(impianto["_id"])
    return impianti

@router.get("/impianti/{id}")
async def get_plant(id: str):
    impianto = plant_collection.find_one({"_id": ObjectId(id)})
    if impianto:
        impianto["_id"] = toString(impianto["_id"])
        return impianto
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Impianto non trovato")

@router.post("/impianti")
async def create_plant(impianto: Impianti):
    response = plant_collection.insert_one(impianto.model_dump())

    return {"_id": toString(response.inserted_id)}