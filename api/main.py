from fastapi import FastAPI
from Routers import endpoints

# Init the API
bane = FastAPI()

# Include routers
bane.include_router(endpoints.router)


# Create root endpoint

@bane.get("/")
def raiz():
    return {
        "message": "Bienvenido al manantial de Fatboy98!"
    }
