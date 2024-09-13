from fastapi import FastAPI, Body
import uvicorn

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'english'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'pakstudy'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'urdu'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Five', 'category': 'math'}
]

@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/{book_title}")
async def read_books(book_title : str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book

@app.get("/books/mybook")
async def read_all_books():
    return {'book_title':'my favorite book'}


@app.get("/books/{book_author}")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
                book.get('category').casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return


@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)

    return new_book



@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS [i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book


@app.delete("/books/{book_title}")
async def delete_book(book_title: str):
        for i in range(len(BOOKS)):
            if BOOKS [i].get('title').casefold() == book_title.casefold():
                BOOKS.pop(i)
                break


if __name__ == "__main__":
    uvicorn.run("books:app", host="0.0.0.0", port=9000, reload=True)