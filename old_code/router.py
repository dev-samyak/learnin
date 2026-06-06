from fastapi import FastAPI
app = FastAPI()

@app.get("/api/funds")
def list_funds(search: str = ""):
    # Logic: SELECT * FROM funds WHERE scheme_name LIKE %search%
    return {"status": "success", "data": [...]}

@app.get("/api/fund/{code}/history")
def get_history(code: str):
    # 1. Check your DB for history first (Cost Saving!)
    # 2. If DB is empty, fetch from API:
    url = f"https://api.mfapi.in/mf/{code}"
    response = requests.get(url).json()
    
    # 3. Save to DB so next time it's instant
    # save_to_db(response['data'])
    

    
    return response['data']