from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get("/")
def root():
    return {"status": "GeoFusiQ API 서버 정상 작동 중 🚀"}

@app.get("/api/parcel/search")
def search_parcel(address: str = Query(...)):
    api_key = "0F9F83ED-D1D4-3691-A909-51D894078AD6"  # 여기에 너의 키 입력
    url = "https://api.vworld.kr/req/address"

    params = {
        "service": "address",
        "request": "getCoord",
        "version": "2.0",
        "crs": "epsg:4326",
        "address": address,
        "format": "json",
        "type": "road",
        "key": api_key
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; GeoFusiQ-Server/1.0)"
    }

    try:
        res = requests.get(url, params=params, headers=headers, timeout=10)

        # 응답 본문 확인 및 JSON 파싱 처리
        if res.status_code == 200:
            try:
                data = res.json()
                return data
            except ValueError:
                return {
                    "에러": "응답 본문이 JSON이 아닙니다",
                    "본문": res.text[:300]
                }
        else:
            return {
                "에러": f"HTTP 상태 코드 {res.status_code}",
                "본문": res.text[:300]
            }

    except Exception as e:
        return {"에러": str(e)}
