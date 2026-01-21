import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

URL = "https://api.coingecko.com/api/v3/coins/markets"

def extract() -> pd.DataFrame:
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 200,
        "page": 1,
        "sparkline": "false"
    }

    headers = {
        "x-cg-demo-api-key": os.getenv("COINGECKO_API_KEY")
    }

    response = requests.get(URL, headers=headers, params=params)
    response.raise_for_status()

    return pd.DataFrame(response.json())


if __name__ == "__main__":
    df = extract()
    print(df.head())
