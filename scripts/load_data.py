import sqlite3
import pandas as pd

# Connect to SQLite DB
conn = sqlite3.connect('../data/supermarket_sales.db')
cursor = conn.cursor()


with open('../sql/create_tables.sql', 'r') as f:
    create_tables_sql = f.read()
cursor.executescript(create_tables_sql)
conn.commit()


dim_date_df = pd.read_csv('../data/dim_date.csv')
dim_product_df = pd.read_csv('../data/dim_product.csv')
fact_sales_df = pd.read_csv('../data/fact_sales.csv')


dim_date_insert = dim_date_df[['date_key','Date','day_of_week','month','year']].copy()
dim_date_insert.rename(columns={'Date':'date'}, inplace=True)
dim_date_insert.to_sql('dim_date', conn, if_exists='append', index=False)

dim_product_insert = dim_product_df[['product_key','Product line','Unit price']].copy()
dim_product_insert.rename(columns={'Product line':'product_line','Unit price':'unit_price'}, inplace=True)
dim_product_insert.to_sql('dim_product', conn, if_exists='append', index=False)

fact_sales_df.to_sql('fact_sales', conn, if_exists='append', index=False)

conn.commit()
conn.close()

print("Data loaded into SQLite database successfully.")
