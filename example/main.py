from fastapi import FastAPI, HTTPException
import uvicorn

import user_service

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users")
async def get_users():
    error = "True"
    return error.split(" ")

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    try:
        user = user_service.get_user_from_db(user_id)
    except user_service.UserNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return user

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=3000, reload=True)