from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="Todo API")

Instrumentator().instrument(app).expose(app)

todos = []


class Todo(BaseModel):
    title: str
    done: bool = False


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/ready")
def ready():
    return {"status": "ready"}


@app.get("/todos")
def get_todos():
    return todos


@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo)
    return todo


@app.put("/todos/{index}")
def update_todo(index: int, todo: Todo):
    if index >= len(todos):
        raise HTTPException(status_code=404, detail="Todo not found")
    todos[index] = todo
    return todo


@app.delete("/todos/{index}")
def delete_todo(index: int):
    if index >= len(todos):
        raise HTTPException(status_code=404, detail="Todo not found")
    todos.pop(index)
    return {"message": "deleted"}
