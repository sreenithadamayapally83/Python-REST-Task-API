from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    completed: bool = False

tasks_db = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the IBM Candidate Task API"}

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks_db

@app.post("/tasks")
def create_task(task: Task):
    tasks_db.append(task)
    return {"message": "Task created successfully"}