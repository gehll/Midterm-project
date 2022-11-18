from fastapi import APIRouter, HTTPException, Query
from database.mongodb import BCN
from Routers.extras import transports, transform


# Init router
router = APIRouter()


'''
Router to get desired collectiong from mongodb. Currently working with: geo_transports and transports_unwind
'''


@router.get("/collection/{name}")
def get_data(name):
    data = BCN[name]
    return transform(data.find({}))


'''
Roiter to get a specific type of transport from geo_transports
'''


@router.get('/transport_type/{type}')
def get_transport_type(type):
    data = BCN['geo_transports']
    type_json = transform(data.find({'Code': {"$in": transports[type]}}))

    return type_json


'''
This routers does the same as the previous but gets only a sample from all documents.
Limit = 0 is equal to setting no limit. rawData = 1 so that default endpoint if to plot map in streamlit
'''


@router.get('/sample/{type}')
def get_transport_type_sample(type, limit: int = 0, rawData: int = 1):
    data = BCN['geo_transports']

    if type == 'Bus' and rawData:
        type_json = transform(
            data.find({'Code': {"$in": transports[type]}}).limit(50))

    else:

        # Validate number of documents to retreive
        if limit < 0 or rawData not in [0, 1]:
            raise HTTPException(
                status_code=400, detail='Limit must be positive and rawData between 0, 1')

        type_json = transform(
            data.find({'Code': {"$in": transports[type]}}).limit(limit))

    return type_json


'''
Router to make geoquery given a location, type of transport and desired lines from that type of transport
'''


@router.get("/geoquery")
def make_geoquery(type: str = 'Metro',
                  location: list[str] = Query(
                      default=['41.40', '2.17']),
                  lines: list[str] = Query(default=['L1', 'L9', 'L7', 'L10', 'BLAU'])):

    # Get the coords
    lat = float(location[0])
    long = float(location[1])

    # The coords will be used as the reference point to make geoqueries and center the output map
    reference = {
        "type": "Point",
        # Geoqueries are made in long, lat format
        "coordinates": [long, lat]
    }

    # Now the filter to get closests stations by type and desired lines

    filt = {
        "Code": {"$in": transports[type]},
        "Lines": {"$in": lines},
        "Location": {
            "$near": {
                "$geometry": reference,
                "$maxDistance": 20000
            }
        }
    }

    # Get the 5 closest ones
    return transform(BCN['geo_transports'].find(filt).limit(5))
