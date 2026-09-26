# Starter Code: Building REST APIs with FastAPI

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Book Catalog API")


class BookCreate(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)


books = [
    {"id": 1, "title": "The Hobbit", "author": "J. R. R. Tolkien"},
    {"id": 2, "title": "A Wrinkle in Time", "author": "Madeleine L'Engle"},
]


@app.get("/books")
def list_books():
    """Return all books in the catalog."""
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int):
    """Return one book by ID."""
    pass


@app.post("/books", status_code=201)
def create_book(book: BookCreate):
    """Create and return a new book."""
    pass


@app.put("/books/{book_id}")
def update_book(book_id: int, book: BookCreate):
    """Update and return an existing book."""
    pass


# Run with:
# uvicorn starter-code:app --reload
