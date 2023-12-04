from fastapi import FastAPI

# fastapi 객체 생성
app = FastAPI()

# 기본 요청(/ 주소에 get 요청)이 오면 수행
# 요청에 따라 아래의 함수를 수행하고 결과를 리턴함
@app.get("/")
async def welcomefunc() -> dict:
    return {
        "message" : "welcome message"
    }