DROP TABLE IF EXISTS fact_sales;
DROP TABLE IF EXISTS dim_product;
DROP TABLE IF EXISTS dim_date;

CREATE TABLE dim_date (
    date_key INTEGER PRIMARY KEY,
    date TEXT,
    day_of_week TEXT,
    month INTEGER,
    year INTEGER
);

CREATE TABLE dim_product (
    product_key INTEGER PRIMARY KEY,
    product_line TEXT,
    unit_price REAL
);

CREATE TABLE fact_sales (
    sales_id TEXT PRIMARY KEY,
    date_key INTEGER,
    product_key INTEGER,
    branch TEXT,
    quantity INTEGER,
    gross_income REAL,
    FOREIGN KEY (date_key) REFERENCES dim_date(date_key),
    FOREIGN KEY (product_key) REFERENCES dim_product(product_key)
);
