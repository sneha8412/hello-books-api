from app import db
from flask import Blueprint, Response
from flask import request
from flask import jsonify
from .models.book import Book


books_bp = Blueprint("books", __name__, url_prefix="/books")

def is_int(value):
    try:
        return int(value)
    except ValueError:
        return False


@books_bp.route("/<book_id>", methods=["GET"], strict_slashes=False)
def get_single_book(book_id):
    #try to find the book with the given Id
    if not is_int(book_id):
        return {
            "message": "id must be an integer",
            "success": False
        },400
        
    book = Book.query.get(book_id)
    
    if book == None:
        return Response("",status=404)
    
    if book:
        return  book.to_json(), 200
    
    return {
        "message": f"Book with id {book_id} was not found",
        "success": False
    }, 404
    
    
    
@books_bp.route("", methods=["GET"], strict_slashes=False)
def books_index():
    
    books = []
    title_query = request.args.get("title")
    
    if title_query is not None:
        book_title = title_query
        books = Book.query.filter_by(title=title_query) # we can put multiple query parameters, books is an instance of class Book
    else:
        books = Book.query.all()
        
    books_response = [] 
    for book in books:
        books_response.append(book.to_json())
        return jsonify(books_response), 200


@books_bp.route("", methods=["POST"], strict_slashes=False)
def books():
    request_body = request.get_json()
    new_book = Book(title=request_body["title"],
                        description=request_body["description"])

    db.session.add(new_book)
    db.session.commit()
    
    return {
        "success": True,
        "message": f"Book {new_book.title} has been created"
    }, 201
    
@books_bp.route("/<book_id>", methods=["PUT"], strict_slashes=False)
def update_book(book_id):
    book = Book.query.get(book_id)
    
    if book == None:
        return Response("", status=404)
    
    if book: 
        form_data = request.get_json()

        book.title = form_data["title"]
        book.description = form_data["description"]

        db.session.commit()

        return Response(f"Book #{book.id} successfully updated", status=200)
    
@books_bp.route("/<book_id>", methods=["DELETE"], strict_slashes=False)    
def delete_single_book(book_id):
    book = Book.query.get(book_id)
    
    if book == None:
        return Response("", status=404)
    
    if book:
        db.session.delete(book)
        db.session.commit()
        return Response(f"Book #{book.id} successfully deleted", status=200)

    #return (f"book #{new_book.title} has been created", 201)
    
    
    
    
    
'''hello_world_bp = Blueprint("hello_world", __name__) #name of the blueprint is hello_world, universal __name__identifies the root filfe in your folder, Blueprint is the name of the class

@hello_world_bp.route('/hello-world', methods = ["GET"])
def get_hello_world():
    my_response = "Hello, World!"
    return my_response

@hello_world_bp.route('/hello-world/JSON', methods=["GET"])
def hello_world_json():
    return{
        "name": "Sneha Agarwal",
        "message": "Heya!",
        "hobbies": ["Coding" , "playing guitar", "hiking"],
    }, 200

@hello_world_bp.route("/broken-endpoint-with-broken-server-code")
def broken_endpoint():
    response_body = {
        "name": "Ada Lovelace",
        "message": "Hello!",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
    }
    new_hobby = "Surfing"
    response_body["hobbies"]+ [new_hobby]
    return response_body'''