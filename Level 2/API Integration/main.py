# main script for API handling and displaying crypto prices
from utils.api_handler import fetch_crypto_price 

def main():
    print("== Fetching Cryptocurrency Price ==")
    crypto_info = fetch_crypto_price()
    if crypto_info:
        print(f"{crypto_info['crypto']} price in {crypto_info['currency']}: ${crypto_info['price']}")
    else:
        print("Failed to fetch crypto price.")

if __name__ == "__main__":
    main()