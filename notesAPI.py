from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
from typing import List
from datetime import date

app = FastAPI()

class Notes(BaseModel):
    id: int
    date: date
    title: str
    note: str 

store: List[Notes]=[] 


@app.get("/")
def home():
    return{"messsage": "homepage of the notes api"}


@app.get("/notes")
def return_():
    return store


@app.post("/notes")
def create_notes(notes:Notes):
    for existing_note in store:
        if existing_note.id == notes.id:
            raise HTTPException(
                status_code=400,
                detail= "ID already exists"
            )
    store.append(notes)
    return notes 

@app.put("/notes/{id}")
def upd(id:int, updates_notes: Notes):
    for sn, notes in enumerate(store):
        if notes.id == id:
            store[sn]= updates_notes
            return updates_notes
    raise HTTPException(
        status_code= 404,
        detail= "note not found"
    )

@app.delete("/notes/{id}")
def delete_notes(id:int, ):
    for sn, notes in enumerate(store):
        if notes.id == id:
            deleted_notes = store.pop(sn)
            return deleted_notes
    raise HTTPException(
        status_code=404,
        detail= "note not found to delete"
    ) 

@app.get("/notess/{id}")
def return_single(id:int):
    for notes in store:
        if notes.id == id:
            return notes 
    raise HTTPException(
        status_code= 404,
        detail= "notes not found"
    )



         
    




