from fastapi import APIRouter, HTTPException #API router is a mini API module for endpoints used to escape monolithic approach of coding
from app.schemas import Task

router = APIRouter() #object for APIRouter


tasks = [] #simple database for now

@router.get("/tasks") #endpoint for getting all tasks
def get_tasks():
    return tasks

@router.get("/tasks/{task_id}")
def get_task(task_id : int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code = 404, detail = "Task not found")

@router.post("/tasks") #endpount for creating a task
def create_task(task : Task):
    new_task = {
        "id" : len(tasks) + 1,
        "title" : task.title,
        "description": task.description,
        "completed": task.completed
    }

    tasks.append(new_task)
    return new_task

@router.put("/task/{task_id}")
def update_task(task_id : int, updated_task: Task):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = updated_task.title
            task["description"] = updated_task.description
            task["completed"] = updated_task.completed
            return task
    raise HTTPException(status_code = 404, detail = "Task not found")


@router.delete("/tasks/{task_id}")
def delete_task(task_id : int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"message": "task deleted"}
        
    raise HTTPException(status_code = 404, detail = "Task not found")