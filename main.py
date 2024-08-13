from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# 데이터베이스 연결 (예: MongoDB, PostgreSQL)
# ...

@app.post("/register/")
async def create_user(user: User):
    # 입력 데이터 유효성 검사
    if await check_user_exists(user.username):
        raise HTTPException(status_code=400, detail="User already exists")

    # 비밀번호 암호화
    hashed_password = get_hashed_password(user.password)
    user.password = hashed_password

    # 데이터베이스에 저장
    await database.save_user(user)
    return {"message": "User created successfully"}
