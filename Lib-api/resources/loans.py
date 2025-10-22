from flask import Blueprint, jsonify, request
import uuid
from datetime import date

loans_bp = Blueprint("loans", __name__)

loans = [
    {"id": "1", "bookId": "1", "memberId": "1", "dateBorrowed": "2025-10-20", "status": "active"}
]


@loans_bp.route("/", methods=["GET"])
def get_loans():
    return jsonify(loans)


@loans_bp.route("/<loan_id>", methods=["GET"])
def get_loan(loan_id):
    loan = next((l for l in loans if l["id"] == loan_id), None)
    if not loan:
        return jsonify({"error": "Loan not found"}), 404
    return jsonify(loan)


@loans_bp.route("/", methods=["POST"])
def create_loan():
    data = request.get_json()
    new_loan = {
        "id": str(uuid.uuid4()),
        "bookId": data.get("bookId"),
        "memberId": data.get("memberId"),
        "dateBorrowed": str(date.today()),
        "status": "active",
    }
    loans.append(new_loan)
    return jsonify(new_loan), 201


@loans_bp.route("/<loan_id>", methods=["DELETE"])
def delete_loan(loan_id):
    global loans
    loans = [l for l in loans if l["id"] != loan_id]
    return "", 204
