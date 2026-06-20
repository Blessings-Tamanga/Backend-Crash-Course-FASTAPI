from pydantic import BaseModel


class BorrowRequest(BaseModel):
    student_id: int
    book_id: int
    librarian_id: int

class UpdateBorrow(BaseModel):
    student_id : int
    book_id : int
    librarian_id : int
    status : str

