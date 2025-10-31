from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get("/")
def root():
    return {"status": "GeoFusiQ API 서버 정상 작동 중 🛰️"}

@app.get("/api/parcel/search")
def search_parcel(address: str = Query(...)):
    # ✅ 1. 네 VWorld API 키
    api_key = "0F9F83ED-D1D4-3691-A909-51D894078AD6"

    # ✅ 2. HTTPS 엔드포인트 (반드시 https!)
    url = "https://api.vworld.kr/req/address"

    # ✅ 3. 요청 파라미터 구성
    params = {
        "service": "address",
        "request": "getCoord",
        "version": "2.0",
        "crs": "epsg:4326",   # WGS84 좌표계
        "address": address,
        "format": "json",
        "type": "road",       # 도로명 주소 기준
        "key": api_key
    }

    # ✅ 4. 요청 실행 및 예외 처리
    try:
        res = requests.get(url, params=params, timeout=20, verify=True)

        # 정상 응답인 경우
        if res.status_code == 200:
            try:
                data = res.json()
                return data
            except Exception:
                return {"에러": "VWorld 응답이 JSON 형식이 아닙니다", "본문": res.text[:300]}

        # HTTP 에러 응답
        else:
            return {"에러": f"HTTP 상태 코드 {res.status_code}", "본문": res.text[:300]}

    # 요청 시간 초과
    except requests.exceptions.Timeout:
        return {"에러": "VWorld API 요청 시간이 초과되었습니다 (Timeout)"}

    # 그 외 예외 처리
    except Exception as e:
        return {"에러": str(e)}
