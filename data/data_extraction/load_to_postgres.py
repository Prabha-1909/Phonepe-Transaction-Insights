import pandas as pd
from sqlalchemy import create_engine

# 1. PostgreSQL connection
engine = create_engine(
    "postgresql://postgres:1909@localhost:5432/phonepe_db"
)

# 2. Read CSV files (THIS WAS MISSING)
transaction_df = pd.read_csv("transaction_data.csv")
user_df = pd.read_csv("user_data.csv")
insurance_df = pd.read_csv("insurance_data.csv")

# 3. Load to PostgreSQL
transaction_df.to_sql(
    "transaction_data",
    engine,
    if_exists="replace",
    index=False
)

user_df.to_sql(
    "user_data",
    engine,
    if_exists="replace",
    index=False
)

insurance_df.to_sql(
    "insurance_data",
    engine,
    if_exists="replace",
    index=False
)

print("Data loaded into PostgreSQL successfully")

