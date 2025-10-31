from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get("/")
def root():
    return {"status": "GeoFusiQ API 서버 정상 작동 중 🚀"}

@app.get("/api/parcel/search")
def search_parcel(address: str = Query(...)):
    api_key = "0F9F83ED-D1D4-3691-A909-51D894078AD6
"
    url = "https://api.vworld.kr/req/address"  # 반드시 HTTPS

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

    try:
        res = requests.get(url, params=params, timeout=15)
        if res.status_code == 200:
            try:
                return res.json()
            except Exception:
                return {"에러": "VWorld 응답이 JSON 형식이 아닙니다", "본문": res.text[:300]}
        else:
            return {"에러": f"HTTP 상태 코드 {res.status_code}", "본문": res.text[:300]}
    except requests.exceptions.Timeout:
        return {"에러": "VWorld API 요청 시간이 초과되었습니다 (Timeout)"}
    except Exception as e:
        return {"에러": str(e)}
