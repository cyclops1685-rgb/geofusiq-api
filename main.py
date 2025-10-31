import requests
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/")
def root():
    return {"status": "GeoFusiQ API 서버 정상 작동 중 🚀"}

@app.get("/api/parcel/search")
def search_parcel(address: str = Query(...)):
    api_key = "0F9F83ED-D1D4-3691-A909-51D894078AD6"  # 실제 VWorld API 키
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
        data = res.json()
        return data
    except Exception as e:
        return {"에러": str(e)}
