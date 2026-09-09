from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel, Field, field_validator, computed_field
from typing import List, Optional, Dict 

app = FastAPI() 

class Customer(BaseModel):
    id:str
    name:str
    email: str
    @field_validator("email")
    @classmethod
    def email_validator(cls, v):
            if "@" not in v:
                raise ValueError("invalid email")
            if not v.endswith(".com"):
                raise ValueError("invalid email")
    
            return v
    
class product(BaseModel):
    name:str = Field(...)
    category:str
    price:float= Field(gt =0)
    stock: str
    description:Optional[str]

   
    
class address(BaseModel):
    country:str
    city:str
    zip_code:int

class todo(BaseModel):
    task:str
    completed: str
    started: str

class order(BaseModel):
     customer: Customer
     item: List[product]
     quantity: int = Field(gt=0)

     @computed_field
     @property
     def subtotal(self) ->float:
              return(self.quantity * self.price)
     
     @computed_field
     @property
     def total(self) -> float:
        return sum(p.quantity * p.price for p in self.item)
     

   




















