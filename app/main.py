from typing import Union

from fastapi import FastAPI

from api.routes import router as nemo_router

app = FastAPI()

app.include_router(nemo_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

