from flask import Blueprint, jsonify

v1_blueprint = Blueprint("v1", __name__)

@v1_blueprint.route("/users", methods=["GET"])
def get_users():
    return jsonify({"users": ["Alice", "Bob", "Charlie"]})
