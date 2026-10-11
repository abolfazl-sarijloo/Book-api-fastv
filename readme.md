# Books API

A simple project for practicing API development with **FastAPI** and data validation with **Pydantic**. This project allows you to manage books through HTTP endpoints.

## Features

- Retrieve a list of books
- Retrieve a specific book by its index
- Add a new book
- Delete a book
- Fully or partially update book information, depending on the implemented endpoint

## Technologies

- Python
- FastAPI
- Pydantic
- Uvicorn

## Data Models

The models are defined in `models.py`.

### `Book`

The model used to create a new book.

| Field | Type | Required? | Description |
|---|---|---|---|
| `name` | `str` | Yes | The name of the book |
| `description` | `str \| None` | No | A description of the book |
| `price` | `float` | Yes | The price of the book |
| `author` | `str` | Yes | The author's name |
| `subject` | `str` | Yes | The subject or category of the book |

### `BookUpdate`

The model used for partially updating a book. All fields are optional, allowing you to send only the fields you want to modify.

For example, the following request updates only the book's price:

```json
{
  "price": 350
}
```

To ensure that a PATCH request updates only the fields explicitly provided by the client, use `model_dump(exclude_unset=True)` in the endpoint and merge the resulting values with the existing book data.

## Installation and Setup

### 1. Create a Virtual Environment (Recommended)

On Windows using PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 2. Install Dependencies

```powershell
pip install fastapi uvicorn
```

### 3. Run the Application

If your FastAPI application is defined in `main.py`, run:

```powershell
uvicorn main:app --reload
```

If your Python file has a different name, replace `main` with your filename.

The `--reload` option automatically restarts the development server whenever you make changes to your code.

## API Documentation

Once the application is running, interactive API documentation is available at the following URLs:

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## API Endpoints

The following endpoints reflect the current implementation described in this project.

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/books` | Retrieve all books |
| `GET` | `/books/{book_id}` | Retrieve a book by its index |
| `POST` | `/books/{book_id}` | Add a new book |
| `DELETE` | `/books/{book_id}` | Delete a book by its index |
| `PATCH` | `/books/{book_id}` | Partially update a book |

### Example: Create a Book

Example request body:

```json
{
  "name": "Learning Python",
  "description": "An introduction to Python",
  "price": 350,
  "author": "Mark Lutz",
  "subject": "Programming"
}
```

## Important Notes

- **Index-based identification:** The `book_id` parameter represents a Python list index. The first book has index `0`, the second has index `1`, and so on.
- **In-memory storage:** Book data is stored in a Python list named `li`. All data will be lost when the application stops or restarts.
- **POST endpoint:** The current `POST /books/{book_id}` endpoint receives a `book_id` parameter but does not use it to add the book. For a simpler REST API design, consider changing the endpoint to `POST /books`.
- **Error handling:** Use FastAPI's `HTTPException` to return appropriate HTTP status codes, such as `404 Not Found` when a book does not exist, instead of returning raw errors or successful responses for failed operations.
- **Database integration:** For a real-world application, consider using a database and assigning each book a unique identifier instead of relying on list indexes.

## Project Goal

This project is designed to help beginners understand the fundamentals of building REST APIs, defining data models, validating request data, and working with HTTP methods in FastAPI.