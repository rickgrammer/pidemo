import pymongo
from flask import Flask, request, jsonify

app = Flask(__name__)
client = pymongo.MongoClient("mongodb+srv://test:test@cluster0.smqmf.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

books = [
    {
    'book_id': 1,
    'book_title': 'tilte',
    'board': 'CBSE',
    'chapter_ids': [1,2,3,4],
    }
]

chapters = [
    {
    'book_id': 1,
    'chapter_id': 1,
    'chapter_name': 'hi',
    'section_ids': [1,2,3,4],
    }
]

sections = [
    {
    'chapter_id': 1,
    'section_id': 1,
    'section_name': 'sec',
    'section_text': 'lorem',
    }
]

@app.route('/')
def index():
    return jsonify({'message': 'GET /books\nGET /books/<book-id>'})

@app.route('/books/')
def books():
    books = db['books']
    return jsonify(list(books.find({}, {'_id': 0})))

@app.route('/books/<int:book_id>/')
def book(book_id):
    books = db['books']
    return jsonify(books.find_one({'book_id': book_id}, {'_id': 0}))

@app.route('/books/<int:book_id>/chapters/')
def chapters(book_id):
    chapters = db['chapters']
    return jsonify(list(chapters.find({
        'book_id': book_id,
    }, {'_id': 0})))

@app.route('/books/<int:book_id>/chapters/<int:chapter_id>/')
def chapter(book_id, chapter_id):
    chapters = db['chapters']
    return jsonify(chapters.find_one({
        'book_id': book_id,
        'chapter_id': chapter_id
    }, {'_id': 0}))

@app.route('/books/<int:book_id>/chapters/<int:chapter_id>/sections/')
def sections(book_id, chapter_id):
    sections = db['sections']
    return jsonify(list(sections.find({
        'book_id': book_id,
        'chapter_id': chapter_id,
    }, {'_id': 0})))

@app.route('/books/<int:book_id>/chapters/<int:chapter_id>/sections/<int:section_id>/')
def section(book_id, chapter_id, section_id):
    sections = db['sections']
    return jsonify(sections.find_one({
        'book_id': book_id,
        'chapter_id': chapter_id,
        'section_id': section_id,
    }, {'_id': 0}))




