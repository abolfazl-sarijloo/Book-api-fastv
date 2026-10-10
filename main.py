from fastapi import FastAPI
import models

app = FastAPI()

li = []

@app.get("/books")
async def root():
    return {'message' : 'fast api is working', 'list': li}

@app.get("/books/{book_id}")
async def Getbook(book_id:int):
    if book_id < 0 or book_id >= len(li):
        return {"message": "Book not found"}

    return {'book': li[book_id]}


@app.post("/books/{book_id}")
async def Addbooks(book: models.Book):
    li.append(book)
    return {'status' : 200, 'message':"success", 'list' : li}





@app.delete("/books/{book_id}")
async def Deletebooks(book_id : int):# -> dict[str, Any]:
    if book_id < 0 or book_id >= len(li):
        return {"message": "Book not found"}

    li.pop(book_id) 

    return {'status' : 200, 'message':"success", 'list' : li}


@app.patch("/books/{book_id}")
async def Updatebooks(book_id: int, book: models.BookUpdate):
    if book_id < 0 or book_id >= len(li):
        return {"message": "Book not found"}

    old_book = li[book_id]

    update_data = book.model_dump(exclude_unset=True)

    updated_book = old_book.model_copy(update=update_data)

    li[book_id] = updated_book

    return {
        "status": 200,
        "message": "success",
        "book": updated_book
    }