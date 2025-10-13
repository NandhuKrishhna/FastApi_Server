from pydantic import BaseModel
import uuid
from datetime import datetime
class Book(BaseModel):
    uuid:uuid.UUID
    title: str
    author: str
    year_published: int
    language: str
    created_at:datetime
    updated_at:datetime

class BookCreateModel(BaseModel):
    title: str
    author: str
    year_published: int
    language: str
class BookUpdateModel(BaseModel):
    title: str
    author: str
    year_published: int
    language: str