from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define a pydantic model for data validation 

class Item(BaseModel):
    name : str
    price : float
    is_offer : bool = None
    
    
    
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