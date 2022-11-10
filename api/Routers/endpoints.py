from fastapi import APIRouter, Header
from database.mongodb import BCN

router = APIRouter()

@router.get("/saludo/{name}")
def saludo(name):
    return {
        "saludo": name
    }

@router.get("/{collection}")
def get_data(collection):
    return list(BCN.collection.find({}))