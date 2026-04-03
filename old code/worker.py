import requests
import psycopg2 # or your preferred DB library

def update_daily_navs():
    # 1. Fetch the master list of all schemes
    master_url = "https://api.mfapi.in/mf/latest"
    all_funds = requests.get(master_url).json()

    for fund in all_funds:
        code = fund['schemeCode']
        # 2. Fetch latest NAV for this specific code
        latest_nav = data['data'][0]['nav']
        # 3. UPSERT into your database (Update if exists, else Insert)
        # cursor.execute("INSERT INTO funds ... ON CONFLICT DO UPDATE ...")
        


    print("Daily sync complete.")