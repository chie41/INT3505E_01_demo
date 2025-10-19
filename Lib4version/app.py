from flask import Flask
from Client_server import v1_blueprint
from Stateless import v2_blueprint
from cacheable import v3_blueprint
from Uniform import v4_blueprint

app = Flask(__name__)

# Đăng ký các blueprint
app.register_blueprint(v1_blueprint, url_prefix="/api/v1")
app.register_blueprint(v2_blueprint, url_prefix="/api/v2")
app.register_blueprint(v3_blueprint, url_prefix="/api/v3")
app.register_blueprint(v4_blueprint, url_prefix="/api/v4")

if __name__ == "__main__":
    print("🚀 REST API demo running at: http://127.0.0.1:5000")
    print("📘 Endpoints:")
    print("  GET  /api/v1/users")
    print("  GET  /api/v2/profile   (requires header Authorization: Bearer abc123)")
    print("  GET  /api/v3/products  (cacheable demo)")
    print("  CRUD /api/v4/users     (Uniform Interface)")
    app.run(debug=True)
