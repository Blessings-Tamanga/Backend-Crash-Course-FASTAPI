from fastapi import FastAPI
from app.routes import books


app = FastAPI()
app.include_router(books.router)

@app.get("/")
def get_health():
    return {"message":"API is working   "}