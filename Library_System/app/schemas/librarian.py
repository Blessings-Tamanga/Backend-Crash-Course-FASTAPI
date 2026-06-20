from pydantic import BaseModel
from typing import Optional

class Librarian(BaseModel):
    name : str
    shift : str


class UpdateLibrarian(BaseModel):
    name : Optional[str] = True
    shift : Optional[str] = True
