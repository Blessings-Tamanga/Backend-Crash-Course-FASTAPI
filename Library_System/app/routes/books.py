from fastapi import APIRouter, HTTPException
from app.schemas.book import Book
from app.services.book_service import create_book
from app.database import books


router = APIRouter()

@router.post("/books")
def add_book(book : Book):
    return create_book(book)


@router.get("/books")
def get_books():
    return books


@router.get("/books/{book_id}")
def get_book(book_id : int):
    for book in books:
        if book["id"] == book_id:
            return book
    return {"detail":"Book not found"}

@router.delete("/books/{book_id}")
def delete_books(book_id : int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message": "book deleted"}
    return {"datail": "book not found"}

