from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
from typing import List
from typing import Optional

app = FastAPI()

class Product(BaseModel):
    product_id: int
    name: str
    category:str
    price: float

products:List[Product]= []

@app.get("/")
def home():
    return("Welcome to homepage")


@app.post("/product")
def add_products(product:Product):
   products.append(product)
   return("product added sucessfully")


@app.get("/products/{product_id}")
def get_product(product_id:int):
    for product in products:
      if product.product_id==product_id:
        return product;
    raise HTTPException(status_code=404, detail="product not found")



@app.get("/products")
def get_products(
    limit:int = Query(default=10, le=100),
    category:Optional[str]=None,
    min_price:Optional[float]= None,
    max_price:Optional[float]= None 
    ):
    result= products

    if category is not None:
       result= [product for product in result if product.category==category]

    if min_price is not None:
       result=[product for product in result if product.price >= min_price]

    if max_price is not None:
       result=[product for product in result if product.max_price <= max_price]

    return result[:limit]








    