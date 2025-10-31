from fastapi import FastAPI

app = FastAPI(title="GeoFusiQ API - 첫 서버")

@app.get("/")
def home():
    return {"status": "ok", "message": "GeoFusiQ API 서버가 정상 작동 중입니다."}

@app.get("/api/parcel/search")
def search_parcel(address: str):
    return {
        "입력한_주소": address,
        "결과": "이건 테스트용 가짜 응답입니다. (나중에 실제 좌표정보로 교체 예정)"
    }
