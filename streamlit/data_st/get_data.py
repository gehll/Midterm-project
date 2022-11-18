import requests


def get_collection(collection):
    '''
    Calls the API to request a specific collection from mongodb database
    '''
    return requests.get(f"http://127.0.0.1:8000/collection/{collection}").json()


def get_transport_type(type):
    '''
    Calls the API to request a specific type of transport from all types in geo_transports collection
    '''
    return requests.get(f"http://127.0.0.1:8000/transport_type/{type}").json()


def get_type_sample(type, params: dict):
    '''
    Calls the API to request a specific type of transport from all types in geo_transports collection
    but only gets a sample. The sample parameters are given with "params".
    '''
    if not isinstance(params, dict):
        raise TypeError('Params must be a dictionary')
    return requests.get(f"http://127.0.0.1:8000/sample/{type}", params=params).json()


# Function to make geoquery for the final part of the streamlit app

def make_geoquery(params):
    '''
    Calls the API to request a geoquery given a location, type of transport and desired lines.
    These parameters come inside "params" that must be a  dictionary.
    '''
    if not isinstance(params, dict):
        raise TypeError('Params must be a dictionary')
    return requests.get("http://127.0.0.1:8000/geoquery", params=params).json()
