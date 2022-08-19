from enum import Enum
from fastapi import Query,Path,Body
from typing import Optional,Union,List,Set
from pydantic import BaseModel,HttpUrl,EmailStr

class Item(BaseModel):
    name : str
    description : Optional[str] = None
    price : float
    tax : Optional[float] = None

class User(BaseModel):
    username: str
    full_name: Optional[str] = None
    
class Image(BaseModel):
    url: HttpUrl
    name: str

class Item2(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = set()
    images: Optional[List[Image]] = None

class Offer(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    items: List[Item2]

class Item3(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: List[str] = []

class User3(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Optional[str] = None

class item44(BaseModel):
    item: str
    description: Union[str, None] = None
    price: float
    is_sold: bool = False
    tax: Union[float, None] = 0

    class Config:
        schema_extra = {
            "example": {
                "item": "cellphone",
                "description": "nice",
                "price": 100.5,
                "is_sold": False,
                "tax": 0.5
                }
            }
