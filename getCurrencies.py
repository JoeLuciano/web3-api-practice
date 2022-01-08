import requests

url = "https://api.exchange.coinbase.com/currencies"

headers = {"Accept": "application/json"}

response = requests.request("GET", url, headers=headers)

print(response.text)