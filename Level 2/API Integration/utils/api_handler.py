import requests

def fetch_crypto_price(crypto_id='bitcoin', currency='usd'):
   # Contains the crypto name, currency, and current price.
    
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies={currency}"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to fetch data: {e}")
        return None

    data = response.json()
    
    if crypto_id in data:
        price = data[crypto_id][currency]
        return {
            "crypto": crypto_id.capitalize(),
            "currency": currency.upper(),
            "price": price
        }
    else:
        print("[ERROR] Invalid response received from API.")
        return None