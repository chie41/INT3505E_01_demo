from fastapi import FastAPI
from slowapi import Limiter
from slowapi.util import get_remote_address

# Routers
from routers import payments_v1, payments_v2

# Global limiter
limiter = Limiter(key_func=get_remote_address)

app = FastAPI(
    title="Payment API Versioning Demo",
    version="2.0.0",
)

# Add handler for 429 errors
app.state.limiter = limiter

# Mount versioned APIs
app.include_router(payments_v1.router, prefix="/api/v1")
app.include_router(payments_v2.router, prefix="/api/v2")

@app.get("/")
def root():
    return {"message": "API Versioning Demo (Python FastAPI)"}
