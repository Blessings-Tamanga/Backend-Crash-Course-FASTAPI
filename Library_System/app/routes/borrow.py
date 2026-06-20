from fastapi import APIRouter
from app.schemas.borrow import BorrowRequest
from app.services.borrow_service import borrow_book
from app.database import borrow_records

router = APIRouter()

@router.post("/borrow")
def borrow(request: BorrowRequest):
    return borrow_book(request)

@router.get("/borrow")
def get_borrows():
    return borrow_records