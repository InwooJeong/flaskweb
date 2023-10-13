import json
import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'Dialektik der Aufklärung',
        'author': 'Max Horkheimer',
        'read': True,
        'price': 22000,
        'sweet': 0
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'The Lord of the Rings: The Two Towers',
        'author': 'J. R. R. Tolkien',
        'read': False,
        'price': 17000,
        'sweet': 0
    },
    {
        'id': uuid.uuid4().hex,
        'title': '문학의 숲을 거닐다',
        'author': '장영희',
        'read': True,
        'price': 15000,
        'sweet': 0
    }
]


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong~!')


@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read'),
            'price': post_data.get('price'),
            'sweet': post_data.get('sweet')
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)


@app.route('/books/<book_id>', methods=['PUT', 'DELETE', 'PATCH'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(book_id)
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read'),
            'price': post_data.get('price'),
            'sweet': post_data.get('sweet'),
        })
        response_object['message'] = 'Updated!'
    if request.method == 'DELETE':
        remove_book(book_id)
        response_object['message'] = 'Book removed!'
    if request.method == 'PATCH':
        up_sweet(book_id)

    return jsonify(response_object)


def remove_book(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False


def up_sweet(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            book['sweet'] += 1


if __name__ == '__main__':
    app.run(debug=True)
