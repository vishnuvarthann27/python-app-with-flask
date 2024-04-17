from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (in-memory database)
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"},
    {"id": 3, "title": "Book 3", "author": "Author 3"}
]

# Route to get all books
@app.route('/api/books', methods=['GET'])
def get_books():
    print("Request reached")
    return jsonify(books)

# Route to get a specific book by ID
@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"message": "Book not found"}), 404

# Route to add a new book
@app.route('/api/books', methods=['POST'])
def add_book():
    new_book = request.json
    books.append(new_book)
    return jsonify({"message": "Book added successfully"}), 201

if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = 5000, debug=True)