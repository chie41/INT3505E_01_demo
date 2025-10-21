from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from datetime import datetime, timedelta

# ===================== CONFIG =====================
SECRET_KEY = "super-secret-key-demo"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15  # token hết hạn sau 15 phút

# ===================== APP =====================
app = FastAPI(
    title="JWT Stateless Auth Demo",
    description="Ví dụ xác thực **stateless bằng JWT token** có thể test ngay trong OpenAPI (/docs)",
    version="1.0.0"
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# ===================== TOKEN LOGIC =====================

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token payload")
        return {"username": username, "exp": payload.get("exp")}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")


# ===================== ROUTES =====================

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if not (form_data.username == "alice" and form_data.password == "123"):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": form_data.username},
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/secure-data")
def read_secure_data(token: str = Depends(oauth2_scheme)):
    user = verify_token(token)
    return {
        "message": f"Xin chào {user['username']} 👋! Dữ liệu bảo vệ chỉ bạn mới thấy.",
        "token_expires_at": datetime.utcfromtimestamp(user["exp"]).isoformat() + "Z"
    }


@app.get("/")
def root():
    return {"message": "JWT Stateless Demo đang chạy. Vào /docs để test."}
