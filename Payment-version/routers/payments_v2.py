from fastapi import APIRouter, Request
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

router = APIRouter(
    prefix="/payments",
    tags=["Payments v2"],
)

@router.post("/")
@limiter.limit("20/minute")
async def create_payment_v2(request: Request, body: dict):
    order_id = body.get("orderId")
    total_amount = body.get("totalAmount")
    payment_method = body.get("paymentMethod")

    return {
        "message": "Payment processed (v2)",
        "orderId": order_id,
        "totalAmount": total_amount,
        "paymentMethod": payment_method,
    }
