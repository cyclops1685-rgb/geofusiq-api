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
    api_key = "0F9F83ED-D1D4-3691-A909-51D894078AD6"

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

        # ✅ 올바른 응답 구조 확인
        if "response" in data and "result" in data["response"]:
            result = data["response"]["result"][0]
            x = result["point"]["x"]
            y = result["point"]["y"]
            return {
                "입력한_주소": address,
                "좌표": {"경도": x, "위도": y},
                "출처": "VWorld API"
            }
        else:
            return {"입력한_주소": address, "결과": "좌표를 찾을 수 없습니다."}

    except Exception as e:
        return {"에러": str(e)}
