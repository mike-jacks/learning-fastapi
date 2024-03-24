from fastapi import FastAPI, Query, Path 
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()

todos = [
    {
        "id": 1,
        "activity": "Jogging for 2 hours at 7:00 AM."
        },
    {
        "id": 2,
        "activity": "Writing 3 pages of my new book at 2:00pm"
        }
]

class todoItem(BaseModel):
    id: int
    activity: str

# minimal app - get request
@app.get("/", tags=['ROOT'])
async def root() -> dict:
    return {"data": "Welcome to the root of the todo app!"}
    
    
# Get --> Read Todo
@app.get("/todo", tags=["todos"])
async def get_todo(id: Annotated[list[int], Query()] = []) -> dict[str, object]:
    filtered_todos = todos
    if id != []:
        filtered_todos = [todo for todo in todos if todo["id"] in id]
    if filtered_todos == []:
        return {"data": "Invalid id!"}
    return {"data": filtered_todos}


# Post --> Create Todo
@app.post("/todo", tags=["todos"])
async def add_todo(todo: todoItem) -> dict[str, object]:
    if todo.id in [todo['id'] for todo in todos]:
        return {
            "data": "A todo with this ID already exists!"
        }
    todos.append(todo.model_dump())
    return {
        "data": f"Todo id: {todo.id} has been added!"
    }

# Put --> Update Todo
@app.put("/todo", tags=["todos"])
async def update_todo(todo: todoItem) -> dict[str, object]:
    json_data = todo.model_dump()
    for item in todos:
        if todo.id == item['id']:
            item['activity'] = json_data['activity']
            return {
                "data": f"Todo id: {json_data['id']} has been updated!"
            }
    return {"data": f"Todo id: {json_data['id']} not found!"}

# Delete --> Delete Todo
@app.delete("/todo", tags=["todos"])
async def delete_todo(todo: todoItem) -> dict[str, object]:
    for item in todos:
        if todo.id == item['id']:
            todos.remove(item)
            return {
                "data": f"Todo id: {todo.id} has been deleted!"
            }
    return {
        "data": f"Todo id: {todo.id} not found!"
    }


