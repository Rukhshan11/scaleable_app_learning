from flask import Blueprint, request, jsonify
from model import Book, db

books_blueprint = Blueprint('book_api_routes', __name__, url_prefix='/api/books')


@books_blueprint.route('/all', methods=['GET'])
def get_all_books():
    all_books = Book.query.all()
    result = [book.serialize() for book in all_books]
    response = {'result': result}
    return jsonify(response)

@books_blueprint.route('/create', methods=['POST'])
def book_create():
    try:
        book = Book()
        book.name = request.form['name']
        book.slug = request.form['slug']
        book.image = request.form['image']
        book.price = request.form['price']

        db.session.add(book)
        db.session.commit()
        response = {'message': 'Book Created', 'result': book.serialize()}

    except Exception as e:
        print(str(e))
        response = {'message': 'Error'}

    return jsonify(response)


@books_blueprint.route('/<slug>', methods=['GET'])
def book_details(slug):
    book = Book.query.filter_by(slug=slug).first()
    if book:
        response = {'return':book.serialize()}
    else:
        response = {'message': 'No Books found'}

    return jsonify(response)