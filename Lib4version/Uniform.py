from flask import Blueprint, request, jsonify

v4_blueprint = Blueprint("v4", __name__)

users = [{"id": 1, "name": "Alice"}]

@v4_blueprint.route("/users", methods=["GET", "POST"])
def users_collection():
    if request.method == "GET":
        return jsonify(users)
    elif request.method == "POST":
        new_user = request.json
        if not new_user or "id" not in new_user or "name" not in new_user:
            return jsonify({"error": "Invalid user data"}), 400
        users.append(new_user)
        return jsonify(new_user), 201


@v4_blueprint.route("/users/<int:user_id>", methods=["GET", "PUT", "DELETE"])
def user_item(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": "Not found"}), 404

    if request.method == "GET":
        return jsonify(user)
    elif request.method == "PUT":
        updated = request.json
        if not updated:
            return jsonify({"error": "Invalid data"}), 400
        user.update(updated)
        return jsonify(user)
    elif request.method == "DELETE":
        users.remove(user)
        return '', 204
