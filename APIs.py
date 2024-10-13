from flask import Flask, request, jsonify

app = Flask(__name__)

TOKEN = '123456'
books = {}
book_id_counter = 1

@app.before_request
def authenticate_token():
    token = request.headers.get("Authorization")
    if not token or token != f"Bearer {TOKEN}":
        return jsonify({"error": "Unauthorized"}), 401

@app.route('/books', methods=['POST'])
def add_book():
    global book_id_counter
    data = request.get_json()
    title = data.get('title')
    author = data.get('author')

    if not title or not author:
        return jsonify({"error": "Title and author are required"}), 400

    new_book = {
        "id": book_id_counter,
        "title": title,
        "author": author
    }
    books[book_id_counter] = new_book
    book_id_counter += 1
    return jsonify(new_book), 201

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = books.get(book_id)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(book), 200

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    book = books.get(book_id)
    if not book:
        return jsonify({"error": "Book not found"}), 404

    book['title'] = data.get('title', book['title'])
    book['author'] = data.get('author', book['author'])
    return jsonify(book), 200

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    if book_id not in books:
        return jsonify({"error": "Book not found"}), 404

    del books[book_id]
    return jsonify({"message": "Book deleted"}), 200

@app.route('/books', methods=['GET'])
def list_books():
    return jsonify(list(books.values())), 200

if __name__ == '__main__':
    app.run(debug=True, port=3000)