import requests

def get_collection(collection):
    return requests.get(f"http://127.0.0.1:8000/collection/{collection}").json()

def get_transport_type(type):
    return requests.get(f"http://127.0.0.1:8000/transport_type/{type}").json()
