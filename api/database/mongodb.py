import sys, os
sys.path.append(os.path.abspath('..'))
from pymongo import MongoClient
from config import DBURL

# Conect to mongodb
client = MongoClient(DBURL)

# Get transport data of Barcelona
BCN = client.get_database("BCN")
