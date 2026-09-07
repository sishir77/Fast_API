
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app=FastAPI()

class books(BaseModel):
    id:int
    name:str
    writer:str
    section:str

Books: List[books] = []

@app.get("/")
def home():
    return{"message": "Welcome to the Library API"}


@app.get("/books")
def get_books():
    return Books


@app.post("/books")
def add_book(book:books):
    Books.append(book)
    return{"message":"Book added sucessfully"}

@app.delete("/books/{book_id}")
def delete_book(book_id:int):
    for book in Books:
        if book.id == book_id:
            Books.remove(book)
            return{"message":"Book deleted sucessfully"}

    return{"message":"Book not found"}

@app.put("/books/{book_id}")
def update_book(book_id:int, updated_book:books):
    for book in Books:
        if book.id == book_id:
            book.name = updated_book.name
            book.writer = updated_book.writer
            book.section = updated_book.section
            return{"message": "Book updated sucessfully"}
    return{"message":"Book not found"}

@app.patch("/books/{book_id}")
def update_section(book_id:int, updated_section:books):
    for book in Books:
        if book.id == book_id:
            if updated_section.name is not None:
                book.name = updated_section.name
            if updated_section.writer is not None:
                book.writer = updated_section.writer
            if updated_section.section is not None:
                book.section = updated_section.section

    return{"message":"Book section updated sucessfully"}
















