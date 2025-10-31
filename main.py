from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get("/")
def root():
    return {"status": "GeoFusiQ API 서버 정상 작동 중 🚀"}

@app.get("/api/parcel/search")
def search_parcel(address: str = Query(...)):
    """
    주소를 입력받아 VWorld API로 실제 좌표를 반환하는 기능
    """
    # ✅ 여기에 네 VWorld API 키 입력
    api_key = "여기에_네_API_KEY"

    url = "http://api.vworld.kr/req/address"
    params = {
        "service": "address",
        "request": "getCoord",
        "version": "2.0",
        "crs": "epsg:4326",   # WGS84 좌표계
        "address": address,
        "format": "json",
        "type": "road",       # 도로명주소 기준
        "key": api_key
    }

    try:
        res = requests.get(url, params=params)
        data = res.json()

        if "response" in data and "result" in data["res]()
