from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app= FastAPI()

class works(BaseModel):
    id: int
    title: str
    completed : bool

todo: List[works]=[]

@app.get("/")
def homepage():
    return{"message":"welcome to todo app"}

@app.get("/todos")
def return_to():
    return todo

@app.post("/todos")
def to_dos(todos: works):
    todo.append(todos)
    return todos


@app.put("/todos/{todos_id}")
def upd(todos_id: int, updated_todos: works):
    for index , todos in enumerate(todo):
        if todos.id == todos_id:
            todo[index] = updated_todos
            return updated_todos
    return{"error": "todos not found"}

@app.delete("/todos/{todos_id}")
def delete_todos(todos_id:int):
    for index, todxxx in enumerate(todo):
        if todxxx.id==todos_id:
            deleted= todo.pop(index)
            return deleted
    return{"error": "todos not found"}

@app.get("/todos/{todos_id}")
def one_to(todos_id:int):
    for todo_item in todo:
        if todo_item.id== todos_id:
            return todo_item
    raise HTTPException(
        status_code=404,
        detail={"Message": "ToDo item not found"}
    )


@app.get("/todo/completed")
def finished():
    completed_todo=[]
    for todos in todo:
        if todos.completed ==True:
            completed_todo.append(todos)
            return completed_todo
    raise HTTPException(
        status_code=404,
        detail={"message": "not any task completed"}
    )