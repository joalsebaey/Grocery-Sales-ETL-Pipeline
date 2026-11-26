# Grocery Sales ETL Pipeline

A Python pipeline joins weekly grocery sales with supplementary Parquet data, cleans the records, and exports detailed sales and monthly averages as CSV files.

## Run locally

Clone the project and install its data dependencies in a Python environment.

```sh
git clone https://github.com/joalsebaey/Grocery-Sales-ETL-Pipeline.git
cd Grocery-Sales-ETL-Pipeline
python -m pip install pandas pyarrow
```

Supply the two input files using the paths in [config.py](config.py). Run commands from the repository root.

| Input | Path |
| --- | --- |
| Weekly sales records | `data/raw/grocery_sales.csv` |
| Supplementary data | `data/raw/extra_data.parquet` |

```sh
python main.py
```

The pipeline writes `data/processed/clean_data.csv` and `data/processed/agg_data.csv`. To inspect the processing steps, start with [main.py](main.py), then follow [extraction](src/extract.py), [transformation](src/transform.py), [loading](src/load.py), and [validation](src/validate.py). The [tests](tests) cover the individual stages.
