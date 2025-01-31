import requests

COINGECKO_API_URL = "https://api.coingecko.com/api/v3/simple/price"
GLASSNODE_API_URL = "https://api.glassnode.com/v1/metrics"
GLASSNODE_API_KEY = "your_glassnode_api_key"

def get_crypto_prices():
    """Fetches real-time Bitcoin & Cardano prices from CoinGecko."""
    params = {"ids": "bitcoin,cardano", "vs_currencies": "usd"}
    response = requests.get(COINGECKO_API_URL, params=params).json()
    return {
        "BTC": response["bitcoin"]["usd"],
        "ADA": response["cardano"]["usd"]
    }

def get_glassnode_data():
    url = "https://api.glassnode.com/v1/metrics/transactions/transfers_volume_sum"
    params = {"api_key": "YOUR_GLASSNODE_API_KEY"}

    response = requests.get(url, params=params)

    # ✅ Debug the raw response
    print(f"🔍 Glassnode API Response Status: {response.status_code}")
    print(f"📃 Glassnode API Response Text: {response.text[:500]}")  # Print first 500 chars

    try:
        data = response.json()
        return data
    except requests.exceptions.JSONDecodeError:
        print("❌ ERROR: Glassnode API returned invalid JSON!")
        return None
