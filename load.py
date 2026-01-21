import os
import pandas as pd
import psycopg2
from psycopg2.extras import execute_batch
from dotenv import load_dotenv

load_dotenv()

def load_to_postgres(df: pd.DataFrame) -> None:
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    query = """
        INSERT INTO coins_market (
            id, symbol, name, current_price, market_cap,
            market_cap_rank, total_volume, high_24h, low_24h,
            price_change_percentage_24h, last_updated
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (id) DO UPDATE SET
            current_price = EXCLUDED.current_price,
            market_cap = EXCLUDED.market_cap,
            market_cap_rank = EXCLUDED.market_cap_rank,
            total_volume = EXCLUDED.total_volume,
            last_updated = EXCLUDED.last_updated;
    """

    data = list(df.itertuples(index=False, name=None))

    with conn.cursor() as cur:
        execute_batch(cur, query, data)
        conn.commit()

    conn.close()


if __name__ == "__main__":
    from extract import extract
    from transform import transform

    df = transform(extract())
    load_to_postgres(df)
