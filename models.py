from pydantic import BaseModel

class Book(BaseModel):
    id : int 
    name: str
    description: str | None = None
    price: float
    author: str
    subject: str

class BookUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    author: str | None = None
    subject: str | None = None