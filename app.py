from flask import Flask, jsonify
from flask_cors import CORS

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app)

BOOKS = [
    {
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'isRead': True
    },
    {
        'title': 'Harry Potter',
        'author': 'Rowling',
        'isRead': False
    },
    {
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'isRead': True
    }
]


@app.route('/books', methods=['GET'])
def get_all_books():
    return jsonify({
        'status': 'success',
        'books': BOOKS
    })


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


if __name__ == '__main__':
    app.run()
