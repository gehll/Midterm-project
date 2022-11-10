from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Cargamos el entorno
load_dotenv()

client = MongoClient(os.getenv("url"))
BCN = client.get_database("BCN")
