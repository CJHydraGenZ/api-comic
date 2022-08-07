from turtle import st
from pydantic import BaseModel


class Studen(BaseModel):
    name: str
    email: str
    age: int
    country: str
