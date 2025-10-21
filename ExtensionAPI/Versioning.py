from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Breaking Changes Example")


@app.get("/api/v1/users")
def get_users_v1():
    return [{"id": 1, "name": "Alice"}]

#Change format
@app.get("/api/v2/users")
def get_users_v2():
    return [{"userId": 1, "fullName": "Alice"}]

@app.get("/")
def root():
    return {"message": "API is running! Try /api/v1/users or /api/v2/users"}

if __name__ == "__main__":
    uvicorn.run("Versioning:app", host="127.0.0.1", port=8000, reload=True)
