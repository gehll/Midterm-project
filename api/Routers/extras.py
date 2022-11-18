from bson import json_util
from json import loads


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


def transform(cursor):
    '''
    This function receives a mongodb cursor and transform it to JSON style
    '''
    return loads(json_util.dumps(cursor))
