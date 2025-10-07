from fastapi import FastAPI, Header
from typing import Optional
from pydantic import BaseModel
app = FastAPI()


class CreateBookModel(BaseModel):
    title:str
    author:str
    rating:float

@app.get('/')
async def read_root():
    return {
        "message":"Hello world"
    }
@app.get("/greet")   
async def greet_name(name:Optional[str] = "User", age : int =0) -> dict:
    return {"message":f"Hello {name} age : {age}"}

@app.post("/create-book")
async def create_book(book_data:CreateBookModel):
    return {
        "title":book_data.title,
        "author":book_data.author,
        "rating":book_data.rating
    }

@app.get("/get_headers")
async def get_header(
    accept:str = Header(None),
    content_type :str = Header(None),
    user_agent:str= Header(None),
    host:str = Header(None)
):
    request_header = {}
    request_header["Accept"] = accept
    request_header["Content-type"] = content_type
    request_header["User-agent"] = user_agent
    request_header["Host"] = host
    
    return request_header
    