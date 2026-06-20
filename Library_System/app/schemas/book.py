from pydantic import BaseModel
from typing import Optional

class Book(BaseModel):
    title : str
    author : str
    concept : str
    pages : int
    cost : float


