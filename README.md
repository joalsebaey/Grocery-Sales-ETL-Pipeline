# Grocery Sales ETL Pipeline

A robust Extract-Transform-Load (ETL) pipeline for processing and analyzing grocery store sales data across multiple departments.

## Project Overview

This project implements a complete ETL pipeline for processing retail sales data. It handles data extraction from multiple sources, transforms raw data into a clean format suitable for analysis, and loads processed datasets in CSV format. The pipeline includes built-in validation to ensure data integrity throughout the process.

## Features

- **Data Extraction**: Merge store sales with supplementary data from parquet files
- **Data Transformation**:
  - Handle missing values with appropriate imputation strategies
  - Extract time-based features from date fields
  - Filter data based on business rules
  - Intelligently select relevant columns for analysis
- **Data Aggregation**: Calculate monthly average sales metrics
- **Data Loading**: Export processed data to standardized CSV format
- **Validation**: Verify output data integrity with automated checks

## Project Structure

- `data/`: Directory for raw and processed data files
- `src/`: Source code for the ETL pipeline components
- `tests/`: Unit tests for pipeline functions
- `main.py`: Main script to run the complete ETL pipeline
- `config.py`: Configuration settings for the pipeline

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/grocery-sales-etl.git
cd grocery-sales-etl

# Install dependencies
pip install -r requirements.txt
