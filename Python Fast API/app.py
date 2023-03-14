from fastapi import FastAPI
import uvicorn ##ASGI

api = FastAPI()

@api.get(path="/")
def home():
    return {"home" : "Hello world"}

@api.get(path="/name")
def get_name(name:str):
    return {"uname" : f"your name is : {name}"}

@api.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

if __name__ == "__main__":
    uvicorn.run(app=api)

# to run the app:  uvicorn main:app.py --reload