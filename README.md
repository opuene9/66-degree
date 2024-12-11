Supermarket Sales Data Pipeline
What’s This?

This project takes supermarket sales data from Kaggle, cleans it up, loads it into a database, and then runs a report to show insights. It also includes a plan for how to run this in the cloud.
What You Get

    Scripts to:
        Download the dataset from Kaggle
        Transform it into dimension and fact tables
        Load it into a SQLite database
    SQL scripts to create tables and generate a report
    A cloud architecture diagram for a future-ready solution

How to Run Locally

    Set up your environment

python3 -m venv venv
source venv/bin/activate
pip install kaggle pandas

Make sure you have your Kaggle API key (kaggle.json) set up in ~/.kaggle/.

Download the data

python scripts/download_data.py

Run the ETL

python scripts/etl.py

This creates cleaned CSV files with dimension and fact data.

Load into SQLite

python scripts/load_data.py

Now your SQLite database (supermarket_sales.db) has the data ready.

Check the Report

sqlite3 data/supermarket_sales.db < sql/report_query.sql