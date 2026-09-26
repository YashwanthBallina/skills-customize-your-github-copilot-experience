# 📘 Assignment: Build a Web Client for a FastAPI API

## 🎯 Objective

Build a browser-based book catalog that communicates with the FastAPI REST API from the previous assignment. You will practice making `fetch()` requests, displaying JSON data in the DOM, submitting form data, and handling loading and error states.

## 📝 Tasks

### 🛠️ Display Books from the API

#### Description

Use the provided HTML starter file to load books from the FastAPI server and display them in a readable catalog when the page opens.

#### Requirements

Completed program should:

- Request books from `GET /books` using `fetch()`.
- Display each book's title, author, and ID in the page.
- Show a loading message while the request is in progress.
- Show a clear error message when the API cannot be reached.
- Keep API request and page-rendering logic in separate functions.

### 🛠️ Add a Book Form

#### Description

Create a form that allows a user to submit a new book to the API and refresh the catalog after the book is created.

#### Requirements

Completed program should:

- Include inputs for a book title and author.
- Prevent submission when either input is empty.
- Send the form data as JSON to `POST /books`.
- Set the request `Content-Type` header to `application/json`.
- Display a success message after the API returns a successful response.
- Clear the form and refresh the displayed books after creation.

### 🛠️ Handle API States and Details

#### Description

Improve the client so users receive useful feedback and can request details for an individual book.

#### Requirements

Completed program should:

- Provide a way to view one book using `GET /books/{book_id}`.
- Display a helpful message when a requested book is not found.
- Handle unsuccessful HTTP responses before parsing response data.
- Disable or clearly update controls while a request is in progress.
- Keep the page usable when the API is offline or returns invalid data.
