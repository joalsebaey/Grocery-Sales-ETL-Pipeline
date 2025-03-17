"""
Configuration settings for the ETL pipeline.
"""

# File paths
RAW_DATA_DIR = "data/raw/"
PROCESSED_DATA_DIR = "data/processed/"

# Input files
GROCERY_SALES_FILE = f"{RAW_DATA_DIR}grocery_sales.csv"
EXTRA_DATA_FILE = f"{RAW_DATA_DIR}extra_data.parquet"

# Output files
CLEAN_DATA_FILE = f"{PROCESSED_DATA_DIR}clean_data.csv"
AGG_DATA_FILE = f"{PROCESSED_DATA_DIR}agg_data.csv"

# Processing parameters
SALES_THRESHOLD = 10000  # Minimum weekly sales amount to include
