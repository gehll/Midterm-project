from fastapi import APIRouter
from database.mongodb import BCN
from bson import json_util
from json import loads

# Init router
router = APIRouter()

# Router to get all the desired collection from the database
@router.get("/collection/{name}")
def get_data(name):
    data = BCN[name]
    return loads(json_util.dumps(data.find({})))

# Get the type a specific type of transport
@router.get('/transport_type/{type}')
def get_transport_type(type):

    # Dictionary to filter type of transport by "Code" field
    # Bus has two codes because it includes day-bus and night-bus. These
    # are considered the "regular" buses
    transports = {'Bus': ['K014', 'K015'],
    'Bus_airport': ['K016'],
    'Bus_station': ['K017'],
    'Metro': ['K001'],
    'Railway': ['K002'],
    'Renfe': ['K003'],
    'Airport_train': ['K004'],
    'Maritime_station': ['K008'],
    'Funicular': ['K009'],
    'Cableway': ['K010'],
    'Tramvia': ['K011']
    }

    data = BCN['geo_transports']
    type_json = loads(json_util.dumps(data.find({'Code':{"$in": transports[type]}})))
    return type_json
