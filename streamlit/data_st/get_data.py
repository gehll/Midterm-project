import requests


def get_collection(collection):
    return requests.get(f"http://127.0.0.1:8000/collection/{collection}").json()


def get_transport_type(type):
    return requests.get(f"http://127.0.0.1:8000/transport_type/{type}").json()


def get_type_sample(type, params):
    return requests.get(f"http://127.0.0.1:8000/sample/{type}", params=params).json()


# Function to make geoquery for the final part of the streamlit app

def make_geoquery(params):
    return requests.get("http://127.0.0.1:8000/geoquery", params=params).json()
