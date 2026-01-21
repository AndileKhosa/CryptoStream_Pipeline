import pandas as pd

def transform(df: pd.DataFrame) -> pd.DataFrame:
    columns = [
        "id",
        "symbol",
        "name",
        "current_price",
        "market_cap",
        "market_cap_rank",
        "total_volume",
        "high_24h",
        "low_24h",
        "price_change_percentage_24h",
        "last_updated"
    ]

    df = df[columns].copy()
    df.fillna(0, inplace=True)
    df["last_updated"] = pd.to_datetime(df["last_updated"])

    return df


if __name__ == "__main__":
    from extract import extract
    raw = extract()
    clean = transform(raw)
    print(clean.head())
