from sqlmodel.ext.asyncio.session import AsyncSession
from .schema import BookCreateModel, BookUpdateModel , Book
from sqlmodel import select ,desc
from .models import Book
class BookServices:
    async def get_all_books(self,session:AsyncSession):
        statement = select(Book).order_by(desc(Book.created_at))
        result = await session.exec(statement)
        print("[ ALL BOOKS ]",result)
        return result.all()
    
    async def get_book(self,book_uid:str, session:AsyncSession):
        statement = select(Book).where(Book.uid== book_uid)
        result = await session.exec(statement)
        print(f"Getting specific books id:{book_uid}", book_uid)
        return result.first()
    
    async def create_book(self,book_data:BookCreateModel, session:AsyncSession):
        print(f"[ Printing books data ] -> ", book_data)
        book_data_dict = book_data.model_dump()
        print(f"[ Printing book_data_dict ] -> ", book_data_dict)
        new_book = Book(
            **book_data_dict
        )
        session.add(new_book);
    
    async def update_book(self, book_uid:str ,  update_data:BookUpdateModel,session:AsyncSession):
        pass
    async def delete_book(self,book_uid:str , session:AsyncSession):
        pass