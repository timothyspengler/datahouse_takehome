# Timothy Spengler
# DataHouse Take Home Assignment
# November 24, 2020


from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}