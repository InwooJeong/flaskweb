from flask import Flask, jsonify, request
from flask_cors import CORS

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

BOOKS = [
    {
        'title': 'Demian',
        'author': 'Hermann Hesse',
        'read': True
    },
    {
        'title': 'The Lord of the Rings',
        'author': 'J. R. R. Tolkien',
        'read': False
    },
    {
        'title': 'Harry Potter and the Prisoner of Azkaban',
        'author': 'J. K. Rowling',
        'read': True
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
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)


if __name__ == '__main__':
    app.run(debug=True)
