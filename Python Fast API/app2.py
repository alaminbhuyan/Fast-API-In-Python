import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union


app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get(path="/")
def read_root():
    return {"message": "Hello World"}

@app.get(path="/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}

@app.put(path="/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "item_name": item.name, "price": item.price}

if __name__ == '__main__':
    uvicorn.run(app=app)

# to open interactive page http://127.0.0.1:8000/docs