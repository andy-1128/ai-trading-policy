import requests
from bs4 import BeautifulSoup
import json

crypto_accounts = {
    "BTC": ["cryptowendyo", "jakegagain"],
    "ETH": ["altcoinpost", "mooncoiners"],
    "SOL": ["mooncoiners"],
    "SUI": ["tradeshipuniversity"],
    "XRP": ["cryptocrushshow"]
}

def get_instagram_reel(username):
    url = f"https://ddinstagram.com/{username}/"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        r = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        for a in soup.find_all('a', href=True):
            if '/reel/' in a['href']:
                return a['href']
    except Exception as e:
        print(f"Error fetching from {username}: {e}")
    return ""

def update_reels():
    updated = []
    for symbol, accounts in crypto_accounts.items():
        for user in accounts:
            link = get_instagram_reel(user)
            if link:
                updated.append({
                    "symbol": symbol,
                    "influencer": user,
                    "reel_url": link
                })
                break
    with open("data/crypto_reels.json", "w") as f:
        json.dump(updated, f, indent=2)

if __name__ == "__main__":
    update_reels()