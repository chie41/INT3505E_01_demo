from flask import Blueprint, jsonify, request
import uuid

books_bp = Blueprint("books", __name__)

# Dữ liệu mẫu
books = [
    {"id": str(i), "title": f"Book {i}", "author": f"Author {i}", "available": True}
    for i in range(1, 51)
]


# ---------------------------
# 1️ Offset-Limit Pagination
# ---------------------------
def paginate_offset_limit(items, offset, limit):
    offset = max(offset, 0)
    limit = max(limit, 1)
    return items[offset: offset + limit]


# ---------------------------
# 2️ Page-Size Pagination
# ---------------------------
def paginate_page_size(items, page, page_size):
    start = (page - 1) * page_size
    end = start + page_size
    return items[start:end]


# ---------------------------
# 3️ Cursor-based Pagination
# ---------------------------
def paginate_cursor(items, after, limit):
    start_index = 0  # mặc định bắt đầu từ đầu danh sách

    # Duyệt qua từng phần tử trong danh sách
    for i, b in enumerate(items):
    # Nếu tìm thấy phần tử có id trùng với "after"
        if b["id"] == after:
            # Bắt đầu từ phần tử kế tiếp (i + 1)
            start_index = i + 1
            break  # dừng vòng lặp (vì đã tìm thấy rồi)

    return items[start_index: start_index + limit]


# ---------------------------
# GET /books (có 3 kiểu phân trang)
# ---------------------------
@books_bp.route("/", methods=["GET"])
def get_books():
    # Lấy kiểu phân trang từ query param
    mode = request.args.get("mode", "offset")

    if mode == "offset":
        offset = int(request.args.get("offset", 0))
        limit = int(request.args.get("limit", 10))
        data = paginate_offset_limit(books, offset, limit)
        return jsonify({
            "pagination": {"mode": "offset", "offset": offset, "limit": limit},
            "data": data
        })

    elif mode == "page":
        page = int(request.args.get("page", 1))
        page_size = int(request.args.get("page_size", 10))
        data = paginate_page_size(books, page, page_size)
        total_pages = (len(books) + page_size - 1) // page_size
        return jsonify({
            "pagination": {"mode": "page", "page": page, "page_size": page_size, "total_pages": total_pages},
            "data": data
        })

    elif mode == "cursor":
        after = request.args.get("after")
        limit = int(request.args.get("limit", 10))
        data = paginate_cursor(books, after, limit)
        next_cursor = data[-1]["id"] if len(data) == limit else None
        return jsonify({
            "pagination": {"mode": "cursor", "after": after, "limit": limit, "next": next_cursor},
            "data": data
        })

    else:
        return jsonify({"error": "Invalid pagination mode"}), 400


# ---------------------------
# CRUD cơ bản (giữ nguyên)
# ---------------------------
@books_bp.route("/<book_id>", methods=["GET"])
def get_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(book)


@books_bp.route("/", methods=["POST"])
def create_book():
    data = request.get_json()
    new_book = {"id": str(uuid.uuid4()), **data}
    books.append(new_book)
    return jsonify(new_book), 201


@books_bp.route("/<book_id>", methods=["PATCH"])
def update_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    book.update(request.get_json())
    return jsonify(book)


@books_bp.route("/<book_id>", methods=["DELETE"])
def delete_book(book_id):
    global books
    books = [b for b in books if b["id"] != book_id]
    return "", 204
