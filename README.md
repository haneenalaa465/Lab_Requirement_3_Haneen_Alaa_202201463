# Book API

This is a RESTful API for managing a collection of books. The API allows users to create, retrieve, update, and delete books. Authentication is required for most operations.

# Swagger Editor
![image](https://github.com/user-attachments/assets/3f90d14b-23c5-48ae-b823-4bd3ab1fec60)


## Authentication

This API uses Bearer Token authentication. You will need to provide an access token in the `Authorization` header for all requests that require authentication.

## Endpoints

### Get All Books
- **URL**: `/books`
- **Method**: `GET`
- **Authentication**: Not Required

### Get a Single Book
- **URL**: `/books/{book_id}`
- **Method**: `GET`
- **Authentication**: Not Required
- **URL Parameters**: 
  - `book_id` (integer): The ID of the book to retrieve.

### Create a Book
- **URL**: `/books`
- **Method**: `POST`
- **Authentication**: Required
- **Body Parameters**:
  - `title` (string): Title of the book.
  - `author` (string): Author of the book.

### Update a Book
- **URL**: `/books/{book_id}`
- **Method**: `PUT`
- **Authentication**: Required
- **Body Parameters**:
  - `title` (string): Updated title of the book (optional).
  - `author` (string): Updated author of the book (optional).

### Delete a Book
- **URL**: `/books/{book_id}`
- **Method**: `DELETE`
- **Authentication**: Required

## Postman Collection

To make testing the API easier, you can use the provided Postman collection. Import the following link into Postman:

[Postman Collection URL](https://elements.getpostman.com/redirect?entityId=38976334-74ced563-b123-473e-b441-3bb6b261582b&entityType=collection)

## How to Use the Postman Collection

1. Open Postman.
2. Click `Import` at the top left of the screen.
3. Select `Link`.
4. Paste the link to the collection: `[https://www.postman.com/collections/your-collection-url](https://elements.getpostman.com/redirect?entityId=38976334-74ced563-b123-473e-b441-3bb6b261582b&entityType=collection)`.
5. Click `Continue`, and the collection will be imported.

## Setup and Installation

To run this API locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/haneenalaa465/Lab_Requirement_3_Haneen_Alaa_202201463.git

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
3. Set up your environment variables:
   ```bash
   export FLASK_APP=app.py
   export FLASK_ENV=development
4. Run the API:
   ```bash
   flask run
5. The API will be available at `http://localhost:5000/api`. 
