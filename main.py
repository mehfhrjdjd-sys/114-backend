from typing import Annotated, List , Union
from fastapi import FastAPI, Path,  Body, Cookie, Form
from pydantic import BaseModel, Field

class Item(BaseModel):
     name: str
     description: str | None = Field(
          default = None , title = "The description of the item" , max_length = 100
     )
     price: float = Field(gt = 0 ,description = "The price must be greater than zero")
     tax: float | None =None
     tags : list = [str] = []


app = FastAPI()


@app.post("/login")
async def login(
     username: Annotated[str, Form()],
     password: Annotated[str, Form()],
):
     return ("username": username)


@app.get("/")
async def root():
    return {"message":"Hello world"}


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id":item_id}


'''
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
        return fake_items_db[skip: skip + limit]
'''


fake_items_db = [
     {"item_name": "Foo"},
     {"item_name": "Bar"},
     {"item_name": "Baz"}
]


@app.get("/items/")
async def read_items(ads_id: Annotated[str | None, Cookie()]) -> list[Item]:
     return ("ads_id": ads_id)


'''
@app.post("/items")
async def create_item(item: Item):
     item_dict = item.mode_dump()
     if item.tax is not None:
          price_with_tax = item.price + item.tax
          item_dict.updata({"print_with_tax":price_with_tax})
     return item_dict
'''


@app.post("/items/")
async def create_item(item: Item) -> Item:
     return item


'''
@app.put("/items/{item_id}")
async def updata_item(
     item_id: Annotated[int , Path(title="The ID of the item to get", ge=0, le=1000)],
     q: str | None = None,
     item: Item | None =None,
 ):
     results = {"item_id": item_id}
     if q:
          result.updata({"q": q})
     if item:
          result.updata({"item": item})
     return results
'''

@app.put("/item/{item_id}")
async def updata_item(item_id: int , item: Annotated[Item , Body(embed = True)]):
     results = {"item_id" : item_id ,"item": item}
     return results