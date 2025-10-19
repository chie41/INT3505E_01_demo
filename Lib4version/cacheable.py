from flask import Blueprint, jsonify, make_response

v3_blueprint = Blueprint("v3", __name__)

@v3_blueprint.route("/products", methods=["GET"])
def get_products():
    response = make_response(jsonify({"products": ["Book", "Pen", "Notebook"]}))
    response.headers["Cache-Control"] = "public, max-age=60"
    return response
