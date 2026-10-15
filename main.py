from fastapi import FastAPI
import models
from fastapi import HTTPException

app = FastAPI()

books = {}

@app.get("/books")
async def root():
    try:
        return {'books': books}
    except:
        raise HTTPException(
            status_code=404,
            detail="Book list is empty"
        )

@app.get("/books/{book_id}")
async def Getbook(book_id:int):
    book = books.get(book_id)
    if book:
        return {'status' : 200, 'message':"success", 'book' : book}
    
    raise HTTPException(
        status_code=404,
        detail="book not found"
    )



@app.post("/books/")
async def Addbooks(book: models.Book):
    try:
        books[book.id] = book
        return {'status' : 201, 'message':"created"}
    except:
        raise HTTPException(
            status_code=400,
            detail="adding book was unsuccessful"
        )




@app.delete("/books/{book_id}")
async def Deletebooks(book_id : int):# -> dict[str, Any]:
    try:
        books.pop(book_id) 

        return {'status' : 200, 'message':"success"}
    except:
        return {'status' : 404, 'message':"book not found"}


@app.patch("/books/{book_id}")
async def Updatebooks(book_id: int, book: models.BookUpdate):
    old_book = books[book_id]

    update_data = book.model_dump(exclude_unset=True)

    updated_book = old_book.model_copy(update=update_data)

    books[book_id] = updated_book

    return {
        "status": 200,
        "message": "success",
        "book": updated_book
    }