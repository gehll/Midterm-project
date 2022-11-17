from fastapi import APIRouter, HTTPException, Query
from database.mongodb import BCN
from bson import json_util
from json import loads
from geopy.geocoders import Nominatim

# Init router
router = APIRouter()

# Router to get all the desired collection from the database


@router.get("/collection/{name}")
def get_data(name):
    data = BCN[name]
    return loads(json_util.dumps(data.find({})))


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

# Get specific type of transport


@router.get('/transport_type/{type}')
def get_transport_type(type):
    data = BCN['geo_transports']
    type_json = loads(json_util.dumps(
        data.find({'Code': {"$in": transports[type]}})))

    return type_json

# Get specific type of transport but limiting to 100 documents if it is "Bus" key


@router.get('/sample/{type}')
# limit = 0 is equal to setting no limit. rawData = 1 so that default endpoint if to plot map in streamlit
def get_transport_type_sample(type, limit: int = 0, rawData: int = 1):
    data = BCN['geo_transports']

    if type == 'Bus' and rawData:
        type_json = loads(json_util.dumps(
            data.find({'Code': {"$in": transports[type]}}).limit(50)))

    else:

        # Validate number of documents to retreive
        if limit < 0 or rawData not in [0, 1]:
            raise HTTPException(
                status_code=400, detail='Limit must be positive and rawData between 0, 1')

        type_json = loads(json_util.dumps(
            data.find({'Code': {"$in": transports[type]}}).limit(limit)))

    return type_json


@router.get("/geoquery")
def make_geoquery(location: list[str] = Query(default=['C. de Lope de Vega, 282, 08018 Barcelona'])):

    if len(location) == 1:
        geolocator = Nominatim(user_agent="BCN")
        locator = geolocator.geocode(location[0])
        lat = locator.latitude
        long = locator.longitude
    else:
        lat = float(location[0])
        long = float(location[1])

    # The reference point will be the passed coordinates
    reference = {
        "type": "Point",
        "coordinates": [long, lat]
    }

    q = {"Location": {
        "$near": {
            "$geometry": reference,
            "$maxDistance": 5000
        }
    }
    }

    return loads(json_util.dumps(BCN['geo_transports'].find(q)))
