import pandas as pd
from datetime import datetime


df = pd.read_csv('../data/supermarket_sales.csv')


df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')


dim_date_df = df[['Date']].drop_duplicates().copy()
dim_date_df['date_key'] = dim_date_df['Date'].rank(method='dense').astype(int)
dim_date_df['day_of_week'] = dim_date_df['Date'].dt.day_name()
dim_date_df['month'] = dim_date_df['Date'].dt.month
dim_date_df['year'] = dim_date_df['Date'].dt.year


dim_product_df = df[['Product line', 'Unit price']].drop_duplicates().copy()
dim_product_df['product_key'] = range(1, len(dim_product_df)+1)


fact_sales_df = df.merge(dim_date_df[['Date','date_key']], on='Date') \
                  .merge(dim_product_df[['Product line','product_key']], on='Product line')
fact_sales_df = fact_sales_df[['Invoice ID','date_key','product_key','Branch','Quantity','gross income']]
fact_sales_df.rename(columns={
    'Invoice ID':'sales_id',
    'Branch':'branch',
    'Quantity':'quantity',
    'gross income':'gross_income'
}, inplace=True)


dim_date_df.to_csv('../data/dim_date.csv', index=False)
dim_product_df.to_csv('../data/dim_product.csv', index=False)
fact_sales_df.to_csv('../data/fact_sales.csv', index=False)

print("ETL step completed. Transformed data saved in data folder.")
