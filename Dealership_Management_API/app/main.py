from fastapi import FastAPI
from app.routes import tasks


app = FastAPI(title="Dealership management API")
app.include_router(tasks.router)


@app.get("/")
def health_check():
    return {"message":"api is on"}