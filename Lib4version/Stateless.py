from flask import Blueprint, request, jsonify

v2_blueprint = Blueprint("v2", __name__)

@v2_blueprint.route("/profile", methods=["GET"])
def get_profile():
    token = request.headers.get("Authorization")
    if token != "Bearer abc123":
        return jsonify({"error": "Unauthorized"}), 401
    return jsonify({"user": "Alice", "role": "admin"})
