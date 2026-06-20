from pydantic import BaseModel
from typing import Optional

class Borrow(BaseModel):
    student_id : int
    book_id : int
    librarian_id : int
    status : str

class UpdateBorrow(BaseModel):
    student_id : int
    book_id : int
    librarian_id : int
    status : str

