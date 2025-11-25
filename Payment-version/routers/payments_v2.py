from fastapi import APIRouter

router = APIRouter(
    prefix="/payments",
    tags=["Payments v2"],
)
#Thêm phướng thức ck vào version2
@router.post("/")
async def create_payment_v2(body: dict):
    """
    Updated payment API (v2)
    """
    order_id = body.get("orderId")
    total_amount = body.get("totalAmount")
    payment_method = body.get("paymentMethod")

    return {
        "message": "Payment processed (v2)",
        "orderId": order_id,
        "totalAmount": total_amount,
        "paymentMethod": payment_method,
    }
