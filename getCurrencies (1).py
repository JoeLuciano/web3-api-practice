import requests
import pandas as pd

url = "https://api.exchange.coinbase.com/currencies"

headers = {"Accept": "application/json"}

response = requests.request("GET", url, headers=headers)

cols = ["id","name","min_size","status","message","max_precision","convertible_to",
           "details","symbol","network_confirmations","sort_order","crypto_address_link","crypto_transaction_link","push_payment_methods","group_types","display_name","processing_time_seconds","min_withdrawal_amount","max_withdrawal_amount"]

df = pd.DataFrame(response.json(), columns = cols)

df = df[["id","name","symbol","details"]]

print(df)
