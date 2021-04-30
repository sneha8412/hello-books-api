from flask import Blueprint

hello_world_bp = Blueprint("hello_wprld", __name__) #name of the blueprint is hello_world, universal __name__identifies the root filfe in your folder, Blueprint is the name of the class

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
    return response_body