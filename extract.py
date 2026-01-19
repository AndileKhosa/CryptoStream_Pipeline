import os
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()  # loads .env

API_KEY = os.getenv("COINGECKO_API_KEY")

URL =  "https://api.coingecko.com/api/v3/coins/markets"


headers = {
    "x-cg-demo-api-key": API_KEY
}

params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 50,
    "page": 1,
    "sparkline": "false"
}

response = requests.get(URL, headers=headers, params=params)
df = pd.DataFrame(response.json())

print(df.head())
