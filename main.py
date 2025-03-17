"""
Main script to run the complete ETL pipeline.
"""

import pandas as pd
from src.extract import extract
from src.transform import transform, avg_weekly_sales_per_month
from src.load import load
from src.validate import validation
import config
import os

def create_directories():
    """Create necessary directories if they don't exist."""
    os.makedirs(config.RAW_DATA_DIR, exist_ok=True)
    os.makedirs(config.PROCESSED_DATA_DIR, exist_ok=True)

def run_pipeline():
    """
    Run the complete ETL pipeline:
    1. Extract data from source files
    2. Transform and clean the data
    3. Calculate aggregated metrics
    4. Load data to output files
    5. Validate output files
    """
    print("Starting ETL pipeline...")
    
    try:
        # Check if input file exists
        if not os.path.exists(config.GROCERY_SALES_FILE):
            raise FileNotFoundError(f"Input file not found: {config.GROCERY_SALES_FILE}")
        
        if not os.path.exists(config.EXTRA_DATA_FILE):
            raise FileNotFoundError(f"Input file not found: {config.EXTRA_DATA_FILE}")
            
        # Extract
        print("Extracting data...")
        grocery_sales = pd.read_csv(config.GROCERY_SALES_FILE)
        merged_df = extract(grocery_sales, config.EXTRA_DATA_FILE)
        print(f"Data extracted. Shape: {merged_df.shape}")
        
        # Transform
        print("Transforming data...")
        clean_data = transform(merged_df)
        print(f"Data transformed. Shape: {clean_data.shape}")
        
        # Aggregate
        print("Calculating aggregates...")
        agg_data = avg_weekly_sales_per_month(clean_data)
        print(f"Aggregation complete. Shape: {agg_data.shape}")
        
        # Load
        print("Loading data to output files...")
        load(clean_data, config.CLEAN_DATA_FILE, agg_data, config.AGG_DATA_FILE)
        
        # Validate
        print("Validating output files...")
        clean_data_valid = validation(config.CLEAN_DATA_FILE)
        agg_data_valid = validation(config.AGG_DATA_FILE)
        
        if clean_data_valid and agg_data_valid:
            print("ETL pipeline completed successfully!")
            print(f"Cleaned data saved to: {config.CLEAN_DATA_FILE}")
            print(f"Aggregated data saved to: {config.AGG_DATA_FILE}")
        else:
            print("ETL pipeline completed with validation errors:")
            print(f"Clean data validation: {'Success' if clean_data_valid else 'Failed'}")
            print(f"Aggregated data validation: {'Success' if agg_data_valid else 'Failed'}")
            
    except Exception as e:
        print(f"Error running ETL pipeline: {e}")
        return False
        
    return True

if __name__ == "__main__":
    create_directories()
    run_pipeline()
