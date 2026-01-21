from extract import extract
from transform import transform
from load import load_to_postgres

def run_pipeline():
    raw_df = extract()
    clean_df = transform(raw_df)
    load_to_postgres(clean_df)
    print("ETL pipeline completed successfully")

if __name__ == "__main__":
    run_pipeline()
