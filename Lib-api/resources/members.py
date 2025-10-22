from flask import Blueprint, jsonify, request
import uuid

members_bp = Blueprint("members", __name__)

members = [
    {"id": "1", "name": "Alice", "email": "alice@example.com"},
    {"id": "2", "name": "Bob", "email": "bob@example.com"},
]


@members_bp.route("/", methods=["GET"])
def get_members():
    return jsonify(members)


@members_bp.route("/<member_id>", methods=["GET"])
def get_member(member_id):
    member = next((m for m in members if m["id"] == member_id), None)
    if not member:
        return jsonify({"error": "Member not found"}), 404
    return jsonify(member)


@members_bp.route("/", methods=["POST"])
def create_member():
    data = request.get_json()
    new_member = {"id": str(uuid.uuid4()), **data}
    members.append(new_member)
    return jsonify(new_member), 201


@members_bp.route("/<member_id>", methods=["PATCH"])
def update_member(member_id):
    member = next((m for m in members if m["id"] == member_id), None)
    if not member:
        return jsonify({"error": "Member not found"}), 404
    member.update(request.get_json())
    return jsonify(member)


@members_bp.route("/<member_id>", methods=["DELETE"])
def delete_member(member_id):
    global members
    members = [m for m in members if m["id"] != member_id]
    return "", 204
