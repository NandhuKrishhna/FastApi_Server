from fastapi import APIRouter,status,HTTPException
from typing import List
from src.books.schema import BookCreateModel, BookModel
from src.books.book_collection import books
book_router = APIRouter()

@book_router.get('/', response_model = List[BookModel])
async def get_all_books():
    return books


@book_router.post('/',status_code=status.HTTP_201_CREATED , response_model=BookCreateModel)
async def create_book(book_data: BookCreateModel):
    new_id = books[-1]["id"] + 1 if books else 1
    new_book ={"id":new_id,**book_data.model_dump()}
    books.append(new_book)
    return new_book

@book_router.get('/{book_id}', response_model=BookModel)
async def get_book(book_id:int):
    for book in books:

        if book["id"] == book_id:
            print(f"Matching book found {book}")
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found.")    
    
@book_router.delete('/{book_id}', status_code=status.HTTP_200_OK)
async def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book["id"] == book_id:
            books.pop(index)
            return {"message": "Book deleted successfully."}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"No book found with id {book_id}")