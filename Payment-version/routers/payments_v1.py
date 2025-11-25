from fastapi import APIRouter

router = APIRRouter = APIRouter(
    prefix="/payments",
    tags=["Payments v1"],
)

@router.post("/")
async def create_payment_v1(body: dict):
    """
    Legacy payment API (v1)
    """
    order_id = body.get("orderId")
    amount = body.get("amount")

    return {
        "message": "Payment processed (v1)",
        "orderId": order_id,
        "amount": amount,
        "deprecated": True,
    }
