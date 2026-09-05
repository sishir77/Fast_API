from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


app = FastAPI()


class Product(BaseModel):
    id:int
    name:str
    quantity:str
    price:str
    description:str

products: List[Product] = []


@app.get("/products")
def get_products():
    return products

@app.get("/")
def home():
    return{"message": "Welcome to the site"}







