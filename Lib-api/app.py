from flask import Flask, jsonify
from resources.books import books_bp
from resources.members import members_bp
from resources.loans import loans_bp
from resources.librarians import librarians_bp

app = Flask(__name__)

# Đăng ký Blueprint cho từng resource
app.register_blueprint(books_bp, url_prefix="/books")
app.register_blueprint(members_bp, url_prefix="/members")
app.register_blueprint(loans_bp, url_prefix="/loans")
app.register_blueprint(librarians_bp, url_prefix="/librarians")


@app.route("/")
def index():
    return jsonify({"message": "Library API is running 🚀"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
