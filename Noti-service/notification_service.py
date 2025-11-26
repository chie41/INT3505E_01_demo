from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook/order', methods=['POST'])
def webhook():
    data = request.json
    print("📩 Webhook received:", data)

    # Xử lý logic thông báo
    print("🔔 Notification sent to user!")

    return "", 200

if __name__ == '__main__':
    print("Notification service running on port 4001...")
    app.run(port=4001)
