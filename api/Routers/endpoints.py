from fastapi import APIRouter, Header
from database.mongodb import BCN
from bson import json_util
from json import loads

router = APIRouter()

@router.get("/saludo/{name}")
def saludo(name):
    return {
        "saludo": name
    }

@router.get("/collection")
def get_data():
    data = BCN['accidents']
    return loads(json_util.dumps(data.find({})))