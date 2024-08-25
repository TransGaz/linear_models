import datetime
from typing import Optional
from pydantic import BaseModel


class PetRegister(BaseModel):
    name: str
    surname: str


class PetGet(BaseModel):
    name: str = ""
    photourls: str = ""
    status: str = ""
    category: Optional["CategoryGet"] = None
    tag: Optional["TagGet"] = None

    class Config:
        from_attributes = True


class CategoryGet(BaseModel):
    id: int
    name: str = ""

    class Config:
        from_attributes = True


class TagGet(BaseModel):
    id: int
    name: str = ""

    class Config:
        from_attributes = True
