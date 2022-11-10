from fastapi import FastAPI
from Routers import endpoints

#Iniciamos la API
bane = FastAPI()

#Incluimos los routers del archivo endpoints
bane.include_router(endpoints.router)

# Creamos el endpoint raiz
@bane.get("/")
def raiz():
    return {
        "message": "Bienvenido al manantial de Fatboy98!"
    }

