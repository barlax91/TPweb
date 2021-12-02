from flask import Flask, render_template, jsonify,request, url_for
import json

from numpy import random


app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello my app'


@app.route('/api/books', methods=['GET'])
def index():

    # cree un livre
    book = [
        {
            'id': 1,
            'titre': 'un titre',
        },
        {
            'id': 2,
            'titre': 'un autre titre random',
        }
    ]
    book = json.dumps(book)
    return jsonify(book)


@app.route('/api/books/id', methods=['GET'])
def getBook_id():

    book = [
        {
            'id': 1,
            'titre': 'un titre',

        },
        {
            'id': 2,
            'titre': 'un autre titre random',
        }
    ]

    RandBook = random.randint(0, 1)
    print(RandBook)
    if book[RandBook]['id'] == 1:
        return jsonify(book[RandBook])
    if book[RandBook]['id'] == 2:
        return jsonify(book[RandBook])


@app.route('/api/books/title', methods=['GET'])
def getBook_title():

    book = [
        {
            'id': 1,
            'titre': 'un titre',

        },
        {
            'id': 2,
            'titre': 'un autre titre random',
        }
    ]

    RandBook = random.randint(0, 1)
    print(RandBook)
    if book[RandBook]['title'] == 1:
        return jsonify(book[RandBook])
    if book[RandBook]['title'] == 2:
        return jsonify(book[RandBook])


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
    app.run(debug=True)
