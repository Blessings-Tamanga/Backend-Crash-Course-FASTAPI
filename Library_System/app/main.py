from fastapi import FastAPI
from app.routes import books, students, librarians, borrow

app = FastAPI()

app.include_router(books.router)
app.include_router(students.router)
app.include_router(librarians.router)
app.include_router(borrow.router)

@app.get("/")
def get_health():
    return {"message":"API is working   "}