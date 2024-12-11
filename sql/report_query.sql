SELECT 
    dp.product_line,
    dd.year,
    SUM(fs.gross_income) AS total_gross_income,
    RANK() OVER (PARTITION BY dd.year ORDER BY SUM(fs.gross_income) DESC) AS income_rank
FROM fact_sales fs
JOIN dim_date dd ON fs.date_key = dd.date_key
JOIN dim_product dp ON fs.product_key = dp.product_key
GROUP BY dp.product_line, dd.year;
