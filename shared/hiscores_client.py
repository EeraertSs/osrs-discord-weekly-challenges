import requests

ACCOUNT_TYPES = {
    "normal": "https://secure.runescape.com/m=hiscore_oldschool/index_lite.json",
    "ironman": "https://secure.runescape.com/m=hiscore_oldschool_ironman/index_lite.json",
    "hardcore": "https://secure.runescape.com/m=hiscore_oldschool_hardcore_ironman/index_lite.json",
    "ultimate": "https://secure.runescape.com/m=hiscore_oldschool_ultimate/index_lite.json"
}

# Functie om de JSON data op te halen van de OSRS API
def fetch_hiscores(username, account_type="normal"):
    url = ACCOUNT_TYPES.get(account_type)
    if not url:
        raise ValueError("Onbekend account type.")

    try:
        response = requests.get(url, params={"player": username}, headers={"Accept": "application/json"})
        response.raise_for_status()
        return response.json()  # ← Dit is al perfect in juiste structuur
    except Exception as e:
        print(f"[ERROR] Fout bij ophalen highscores voor {username}: {e}")
        return None

def fetch_skills(username, account_type="normal"):
    data = fetch_hiscores(username, account_type)
    if data and "skills" in data:
        return data["skills"]
    return None

def fetch_activities(username, account_type="normal"):
    data = fetch_hiscores(username, account_type)
    if data and "activities" in data:
        return data["activities"]
    return None
