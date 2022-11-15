import sys, os
sys.path.append(os.path.abspath('..'))
from pymongo import MongoClient
from config import dburl

# Conect to mongodb
client = MongoClient(dburl)

# Get transport data of Barcelona
BCN = client.get_database("BCN")
