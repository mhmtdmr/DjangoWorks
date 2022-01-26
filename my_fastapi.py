
# cmd : # uvicorn my_fastapi:app --reload 

import re
from fastapi import FastAPI,Path, Query,HTTPException,status
from typing import Optional

app = FastAPI()

# GET : READ
# POST : CREATE
# PUT : UPDATE
# DELETE : DELTE

# @app.get("/")
# def home():
#     return {"data":"Test Baby, Test Yo","mata":"Al sana datanın hası"}

# @app.get("/about")
# def about():
#     return {"data":"About"}

inventory = {
    1:
    {
        "name":"Milk",
        "price":11.99,
        "brand":"Sütaş"
    },
    2:
    {
        "name":"Sucuk",
        "price":16.99,
        "brand":"Cumhuriyet"
    }
}

# @app.get("/get-item/{item_id}")
# def get_item(item_id:int):
#     return inventory[item_id]

#http://127.0.0.1:8000/get-item/1
@app.get("/get-item/{item_id}")
def get_item(item_id:int=Path(None)):   # def get_item(item_id:int=Path(None,lt=2)):
    return inventory[item_id]


# # http://127.0.0.1:8000/get-by-name?name=Milk
# @app.get("/get-by-name")
# def get_item(name:str=None):
#     for item_id in inventory:
#         if inventory[item_id]["name"] == name:
#             return inventory[item_id]
#     return {"data":"Not found baby"}


# # http://127.0.0.1:8000/get-by-name?name=Milk
# @app.get("/get-by-name")
# def get_item(name: Optional[str]=None):
#     for item_id in inventory:
#         if inventory[item_id]["name"] == name:
#             return inventory[item_id]
#     return {"data":"Not found baby"}

# # http://127.0.0.1:8000/get-by-name?oglum=bak&name=Milk
# @app.get("/get-by-name")
# def get_item(*,name:Optional[str],test=  ):
#     for item_id in inventory:
#         if inventory[item_id]["name"] == name:
#             return inventory[item_id]
#     return {"data":"Not found baby"}

# # http://127.0.0.1:8000/get-by-name/1?oglum=bak&name=Milk
# @app.get("/get-by-name/{item_id}")
# def get_item(*,item_id:int ,name:Optional[str],test=None):
#     for item_id in inventory:
#         if inventory[item_id]["name"] == name:
#             return inventory[item_id]
#     return {"data":"Not found baby"}


# # http://127.0.0.1:8000/get-by-name?name=Milk
# @app.get("/get-by-name")
# def get_item(name:str = Query(None,title="Name",description="Name of item")):
#     for item_id in inventory:
#         if inventory[item_id]["name"] == name:
#             return inventory[item_id]
#     return {"data":"Not found baby"}



from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

class UpdateItem(BaseModel):
    name: str = None
    price: float = None
    brand: Optional[str] = None

@app.post("/add-item/{item_id")
def add_item(item_id:int,item: Item):
    if item_id in inventory:
        # return {"error":"Item ID already exists."}
        raise HTTPException(status_code=400,detail="ItemID already exists!")
    # inventory[item_id] = {"name":item.name,"brand":item.brand,"price":item.price}
    inventory[item_id] = item
    return inventory[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        # return {"Error":"Item ID does not exsts baby."}
        raise HTTPException(status_code=404,detail="Item ID does not exists man!")
    if item.name != None:
        inventory[item_id]["name"] = item.name
    if item.price != None:
        inventory[item_id]["price"] = item.price
    if item.brand != None:
        inventory[item_id]["brand"] = item.brand
    return inventory[item_id]

@app.delete("/delete-item")
def delete_item(item_id:int = Query(...,description="The ID to delete. ",gt=0)):
    if item_id not in inventory:
        return {"Error":"ID does not exits!"}
    del inventory[item_id]
    return {"Success":"Item deleted!"}
