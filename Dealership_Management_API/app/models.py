from pydantic import BaseModel
from typing import Optional


class VehicleModel(BaseModel):
    name : str
    price : float


class UpdateModel(BaseModel):
    name: Optional[str] = None
    price : Optional[float] = None