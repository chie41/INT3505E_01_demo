import requests
import time

event = {
    "event": "order.paid",
    "orderId": int(time.time()),
    "amount": 450000
}

print("➡️  Sending webhook...")
res = requests.post("http://localhost:4001/webhook/order", json=event)

print("✔️  Webhook delivered:", res.status_code)
