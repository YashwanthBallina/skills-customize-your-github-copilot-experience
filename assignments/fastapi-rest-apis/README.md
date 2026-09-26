# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI to practice HTTP methods, route parameters, JSON responses, and request validation. You will extend the provided book catalog starter code and run the API locally.

## 📝 Tasks

### 🛠️ Create API Routes

#### Description

Use the provided starter code to create routes for reading books in an in-memory catalog.

#### Requirements

Completed program should:

- Start a FastAPI application in `starter-code.py`.
- Return all books from `GET /books` with an HTTP 200 response.
- Return one book from `GET /books/{book_id}`.
- Return an HTTP 404 response when the requested book does not exist.
- Return book data as JSON objects with `id`, `title`, and `author` fields.

### 🛠️ Add Create and Update Operations

#### Description

Add endpoints that allow clients to create a new book and update an existing book in the in-memory catalog.

#### Requirements

Completed program should:

- Define a request model with Pydantic containing a book title and author.
- Add a `POST /books` route that creates a book and returns the new book as JSON.
- Assign each new book a unique integer ID.
- Add a `PUT /books/{book_id}` route that updates an existing book.
- Return an HTTP 404 response when an update targets a missing book.

### 🛠️ Validate and Test the API

#### Description

Add validation and verify each endpoint using FastAPI's interactive documentation or an API client.

#### Requirements

Completed program should:

- Reject a request with an empty title or author using request validation.
- Return an HTTP 422 response for invalid request data.
- Run the server with Uvicorn and make the interactive docs available at `/docs`.
- Test `GET`, `POST`, and `PUT` requests and record one successful response for each.
