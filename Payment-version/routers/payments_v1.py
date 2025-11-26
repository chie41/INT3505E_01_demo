from fastapi import APIRouter, Request
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

router = APIRouter(
    prefix="/payments",
    tags=["Payments v1"],
)

@router.post("/")
@limiter.limit("10/minute")
async def create_payment_v1(request: Request, body: dict):
    order_id = body.get("orderId")
    amount = body.get("amount")

    return {
        "message": "Payment processed (v1)",
        "orderId": order_id,
        "amount": amount,
        "deprecated": True,
    }
