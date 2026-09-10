from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app=FastAPI()


class user(BaseModel):
    id:int
    name:str
    email: str
    password:str

class User(BaseModel):
    id:int
    name:str
    email:str

class product(BaseModel):
    name:str
    category:str
    price:float
    description:str
    customer: User


@app.post("/products", response_model=product)
def create_product(item:product):
    return item

@app.get("/User", response_model=List[User])
def return_user(User):
    return[
        User(id=1, name= "john", email= "john@gmailcom"),
        User(id=2, name="jhoe", email= "jhoe@gmail.com")
     ]

@app.get("/users/{user_id}", response_model= User)
def return_user_out(user_id:int):
    for customer in user:
        if customer.id == user_id:
            return customer






