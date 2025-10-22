from flask import Blueprint, jsonify, request
import uuid

librarians_bp = Blueprint("librarians", __name__)

librarians = [
    {"id": "1", "name": "Librarian A", "email": "liba@example.com"},
    {"id": "2", "name": "Librarian B", "email": "libb@example.com"},
]


@librarians_bp.route("/", methods=["GET"])
def get_librarians():
    return jsonify(librarians)


@librarians_bp.route("/<librarian_id>", methods=["GET"])
def get_librarian(librarian_id):
    librarian = next((l for l in librarians if l["id"] == librarian_id), None)
    if not librarian:
        return jsonify({"error": "Librarian not found"}), 404
    return jsonify(librarian)


@librarians_bp.route("/", methods=["POST"])
def create_librarian():
    data = request.get_json()
    new_lib = {"id": str(uuid.uuid4()), **data}
    librarians.append(new_lib)
    return jsonify(new_lib), 201
