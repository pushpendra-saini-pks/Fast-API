from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import Optional ,List

app = FastAPI()

# Define a pydantic model for data validation 

class Item(BaseModel):
    name : str
    price : float
    is_offer : Optional[bool] = None
    

## IN memory-database 
items = {}
    
# define a basic route 
@app.get("/")

def read_out():
    return {'Hello' : 'Welcome to All'}



# define a route with a path parameter 
@app.post("/items/{item_id}")

def read_item(item_id : int , q:str =None):
    return {"item_id" : item_id ,"q" : q}


# define a route to create an item with post 

@app.post("/")
def create_item(item:Item):
    return {"item_name":item.name,"item_price" : item.price, "item_is_offer":item.is_offer}


@app.post("/items", response_model=Item)
def create_item(item:Item ,item_id:int):
    if item_id in items : 
        raise HTTPException(status_code=400,detail = "Item already exists")
    items[item_id] = item
    return item



@app.get("/items", response_model=Item)
def create_item(item_id:int):
    if item_id not in items : 
        raise HTTPException(status_code=400,detail = "Item Not exists")
    
    return items[item_id]


@app.put("/items", response_model=Item)
def update_item(item_id:int, updated_item:Item):
    if item_id not in items : 
        raise HTTPException(status_code=400,detail = "Item Not exists")
    items[item_id] = update_item
    return update_item


@app.delete("/items/{item_id}", response_model=Item)
def delete_item(item_id:int):
    if item_id not in items : 
        raise HTTPException(status_code=400,detail = "Item already exists")
    deleted_item = items.pop(item_id)
    return deleted_item