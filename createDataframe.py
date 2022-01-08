import requests
import pandas as pd
from datetime import datetime, timedelta

apiUrl = "https://api.pro.coinbase.com"

sym = "ETH-USD"

barSize = "300"

timeEnd = datetime.now()

delta = timedelta(minutes = 5)

timeStart = timeEnd - (300*delta)

timeStart = timeStart.isoformat()
timeEnd = timeEnd.isoformat()

parameters = {
  "start":timeStart,
  "end":timeEnd,
  "granularity":barSize,
}

data = requests.get(f"{apiUrl}/products/{sym}/candles",
                    params=parameters,
                    headers= {"content-type":"application/json"})

df = pd.DataFrame(data.json(),
                  columns = ["time","low","high","open","close","volume"])

df["date"] = pd.to_datetime(df["time"], unit='s')

df = df[["date","open","high","low","close"]]

print(df)
