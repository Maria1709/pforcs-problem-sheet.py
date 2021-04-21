# Author: Maria Carroll
# https://realpython.com/python-bitcoin-ifttt/
# Week
# Lecturer: Andrew Beatty



# Description : Get the current bitcoin price

#Import the requests library
import requests

# get the URL ticker to get the .json file of the crypto currency
TICKER_API_URL = 'https://api.coinmarketcap.com/v1/ticker/'

# Function to get the latest crypto currency price for a secific crypto( bitocin. litecoin, ethereum)
def get_latest_crypto_price(crypto):

    response = requests.get(TICKER_API_URL+crypto)
    response_json = response.json()

    return float(response_json[0]['price_usd']

    # Test the function
get_latest_crypto_price('bitcoin')

def main()

    crypto = "bitcoin"
    price = get_latest_crypto_price(crypto)

    print('Bitcoin Price:',price)

main()
