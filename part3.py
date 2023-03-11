import requests
import time

# Define constants for the API endpoint and currency pair
ENDPOINT = "https://api.pro.coinbase.com"
PRODUCT_ID = "BTC-USD"

# Define the number of seconds between each request to the API
SLEEP_INTERVAL = 60

def get_price():
    """
    Sends a GET request to the Coinbase Pro API to retrieve the current BTC-USD price.

    Returns:
    float: The current price of BTC-USD.
    """
    # Construct the API endpoint URL
    url = f"{ENDPOINT}/products/{PRODUCT_ID}/ticker"

    # Send a GET request to the API endpoint
    response = requests.get(url)

    # If the response is successful, return the price
    if response.status_code == 200:
        data = response.json()
        price = float(data["price"])
        return price

    # If the response is not successful, raise an exception
    else:
        raise Exception(f"Error retrieving price: {response.status_code} - {response.text}")


def main():
    """
    Main function that continuously retrieves the BTC-USD price and prints it to the console.
    """
    print("Starting price tracker...")
    while True:
        try:
            price = get_price()
            print(f"BTC-USD Price: ${price:.2f}")
            time.sleep(SLEEP_INTERVAL)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(SLEEP_INTERVAL)


if __name__ == "__main__":
    main()
