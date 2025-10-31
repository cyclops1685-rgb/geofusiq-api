from fastapi import FastAPI, Query
import requests, time

app = FastAPI()

@app.get("/")
def root():
    return {"status": "GeoFusiQ API 서버 정상 작동 중 ✅"}

@app.get("/api/parcel/search")
def search_parcel(address: str = Query(...)):
    api_key = "0F9F83ED-D1D4-3691-A909-51D894078AD6"
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

    for i in range(3):
        try:
            res = requests.get(url, params=params, timeout=10)
            if res.status_code == 200:
                return res.json()
            else:
                time.sleep(2)
        except Exception as e:
            if i == 2:
                return {"에러": f"VWorld API 연결 실패 (3회 재시도 후 중단)", "내용": str(e)}
            time.sleep(2)

    return {"에러": "예상치 못한 오류 발생"}
