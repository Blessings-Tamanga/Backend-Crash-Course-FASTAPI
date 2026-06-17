from fastapi import FastAPI
from app.routes import tasks

app = FastAPI()
app.include_router(tasks.route)

@app.get("/")
def get_health():
    return {"message":"app is running"}