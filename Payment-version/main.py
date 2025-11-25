from fastapi import FastAPI
from routers import payments_v1, payments_v2

app = FastAPI(
    title="Payment API Versioning Demo",
    version="2.0.0",
)

# Mount versioned routers
app.include_router(payments_v1.router, prefix="/api/v1")
app.include_router(payments_v2.router, prefix="/api/v2")

@app.get("/")
def root():
    return {"message": "API Versioning Demo (Python FastAPI)"}
