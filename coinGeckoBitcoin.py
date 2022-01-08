from pycoingecko import CoinGeckoAPI
import pandas as pd

cg = CoinGeckoAPI()

coin_id = "bitcoin"
coin_ids = ['bitcoin', 'ethereum', 'litecoin']
vs_currency = "usd"
days = "31"

data = cg.get_coin_market_chart_by_id(
    id=coin_id, vs_currency=vs_currency, days=days)

price_df = pd.DataFrame(data["prices"], columns=["time", "price"])
mc_df = pd.DataFrame(data["market_caps"], columns=["time", "market_cap"])
vol_df = pd.DataFrame(data["total_volumes"], columns=["time", "total_volume"])

price_df["date"] = pd.to_datetime(price_df["time"], unit='ms')
mc_df["date"] = pd.to_datetime(mc_df["time"], unit='ms')
vol_df["date"] = pd.to_datetime(vol_df["time"], unit='ms')

price_df = price_df[["date", "price"]]
mc_df = mc_df[["date", "market_cap"]]
vol_df = vol_df[["date", "total_volume"]]

print(price_df)
print(mc_df)
print(vol_df)
