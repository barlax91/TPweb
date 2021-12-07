from flask import Flask, render_template, jsonify, request, url_for
import json

from numpy import random


app = Flask(__name__)


books = [
        {
            'id': 1,
            'titre': 'un titre',
        },
        {
            'id': 2,
            'titre': 'un autre titre random',
        }
    ]
books = json.load(open("books.json"))


@app.route('/')
def home():
    return "Hello my app"


@app.route('/ma_route/<name>', methods=["GET"])
def get_name(name):
    return "Hello"+name


@app.route('/api/books', methods=['GET'])
def index():

    return jsonify(books)


@app.route('/api/books/<int:id>', methods=['GET'])
def getBook_id(id):
    book = None
    for val in books:
        if val.get("isbn") == str(id):
            book = val
            break
    return jsonify(book)


@app.route('/api/books/<string:title>', methods=['GET'])
def getBook_title(title):
    book = None
    for val in books:
        if val.get("title") == title:
            book = val
            break
    return jsonify(book)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
