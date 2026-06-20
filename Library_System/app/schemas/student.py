from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):
    name : str
    classname : str
    active : bool = True


class UpdateStudent(BaseModel):
    name : Optional[str] = True
    classname : Optional[str] = True
    active : bool = True