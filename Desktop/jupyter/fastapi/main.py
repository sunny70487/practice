from enum import Enum
from fastapi import FastAPI,Query,Path,Body
import uvicorn
from typing import Optional,Union,List,Set
from my_model import *

app = FastAPI()
@app.get('/')
async def root():
    return {'message':'Hello world!'}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

@app.get('/file/{file_path:path}')
async def read_file(file_path:str):
    return f'file_path:{file_path}'

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

@app.get('/users/{user_id}/items/{item_id}')
async def read_user_item(user_id : int, item_id : int, q : Optional[str] = None, short : bool = False, needy : str = None):
    item = {"item_id" : item_id, "owner_id" : user_id, "needy" : needy}
    if q:
        item.update({"q" : q})
    if not short:
        item.update({"description": "You are so short"})
    return item

#----------------------Post-------------------------------------


@app.post('/items_p/')
async def create_item(item : Item):
    item_dict = item.dict()
    return item_dict

@app.put('/items_pu/{item_id}')
async def create_item_pu(item_id : int, item: Item):
    return {'item_id':item_id,**item.dict()}

#-----------------------check digit------------------------------

@app.get('/item1/{item_id}')
async def read_items(*,
    item_id: int = Path(title = "The ID the item to get",ge = 10),
    q: Optional[List[str]] = Query(
        default=None,
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,)
):
    results = {"items": [{"item_id": item_id}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.post("/item13/{item_id}")
async def update_item(item_id: int, item: Item, user: User, importance: int = Body(...,embed=True)):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results 


@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer
#----------------------response_model---------------------


@app.post("/items3/", response_model=Item3)
async def create_item(item: Item3):
    return item




@app.post("/user3/", response_model=User3, response_model_include={"username", "email", "full_name"})
async def create_user(user: User3):
    return user



@app.post("/postTest/")
def postTest(item: item44):
    return item

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=2000, reload=True)