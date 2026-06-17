from fastapi import FastAPI #importing fastapi
from app.routes import tasks #importing task routes file in routes forlder

app = FastAPI(title = "Task Manager API") #creating backend instance

app.include_router(tasks.router)  #connecting routes to the main app

@app.get("/")
def home():
    return {"message": "Task Manager API is running"}