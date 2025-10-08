from pydantic import BaseModel
class BookCreateModel(BaseModel):
    title: str
    author: str
    genre: str
    year_published: int
    rating: float
    pages: int
    language: str
class BookModel(BookCreateModel):
    id:int
