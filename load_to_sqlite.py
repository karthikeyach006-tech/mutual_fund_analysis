import pandas as pd # type: ignore
from sqlalchemy import create_engine # type: ignore

engine = create_engine("sqlite:///bluestock_mf.db")

files = {
    "dim_fund": "data/processed/fund_master_clean.csv",
    "fact_nav": "data/processed/nav_history_clean.csv",
    "fact_transactions": "data/processed/investor_transactions_clean.csv",
    "fact_performance": "data/processed/scheme_performance_clean.csv",
    "fact_aum": "data/processed/aum_clean.csv"
}

for table, path in files.items():
    df = pd.read_csv(path)

    df.to_sql(
        table,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"{table} loaded")
    
print("\nDatabase created successfully!")