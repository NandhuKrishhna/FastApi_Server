from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager
from src.db.main import init_db



@asynccontextmanager 
async def life_span(app:FastAPI):
    print(f"[ The server is started ]")
    await init_db()
    yield
    print(f"[ Server has been stopped ]")


version = "v1"

app = FastAPI(
    title="Bookly",
    description="A Rest API for a book service",
    version=version,
    lifespan=life_span
)
app.include_router(book_router, prefix=f"/api/{version}/books",tags=["book"])