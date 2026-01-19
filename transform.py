# transform.py
import pandas as pd

def transform(data):
    """
    Transforms raw CoinGecko data into a clean DataFrame for loading to Postgres.
    """
    # Convert to DataFrame if not already
    if not isinstance(data, pd.DataFrame):
        df = pd.DataFrame(data)
    else:
        df = data.copy()

    # Select only relevant columns
    columns_to_keep = [
        "id", "symbol", "name", "current_price", "market_cap",
        "market_cap_rank", "total_volume", "high_24h", "low_24h",
        "price_change_percentage_24h", "last_updated"
    ]
    
    df = df[columns_to_keep]

    # Optional: handle missing values
    df.fillna(0, inplace=True)

    # Convert last_updated to datetime
    df["last_updated"] = pd.to_datetime(df["last_updated"])

    return df

# --- TESTING ---
if __name__ == "__main__":
    from extract import data  # Import the data you fetched
    df = transform(data)
    print(df.head())

