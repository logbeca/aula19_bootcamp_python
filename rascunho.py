from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool,None] = None

@app.get("/") # response = request.get("http://127.0.0.1:8000/")
def read_root():
    return {"Hello": "World"}

@app.get("/rebeca")
def read_r():
    return {"Rebeca": "Data Engineer"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# APLICAÇÃO renderiza o print no browser 

@app.put("items/{item_id}") #pydantic, mkdocs, unicorn, api
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}



#browser é apenas get
# para dar update ou create, usar postman ou outro. Ou o próprio fastapi