from datetime import date
from pydantic import BaseModel

class VendaBase(BaseModel):
    data: date
    preu: float
    usuarisobrenom: str
    elementvendaid: int

class VendaCreate(BaseModel):
    usuarisobrenom: str
    elementvendaid: int

class VendaRead(VendaBase):
    class Config:
        orm_mode = True
