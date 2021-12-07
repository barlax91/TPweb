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


@app.route('/api/books/catalogue', methods=["POST", "GET"])
def getBooks():
    with open("books.json", "r") as read_file:
        data = json.load(read_file)
    # aleaBook = random.randint(0, len(data))
    # data = json.dumps(data[aleaBook])
    if request.method == "POST":
        livre = request.form["idortitle"]
        for i in range(0, len(data)):
            if data[i]['isbn'] == livre or data[i]['title'] == livre:
                data = json.dumps(data[i])
                return jsonify(data)
            else:
                return render_template('erreurBook.html', title='Fail')

    else:
        return render_template('catalogue.html', title='Catalogue')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
