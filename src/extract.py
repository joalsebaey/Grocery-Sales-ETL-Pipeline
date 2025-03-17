import pandas as pd

def extract(store_data, extra_data_path):
    """
    Extract and merge data from multiple sources.
    
    Parameters:
    -----------
    store_data : pandas.DataFrame
        Main grocery sales data
    extra_data_path : str
        Path to parquet file containing supplementary data
        
    Returns:
    --------
    pandas.DataFrame
        Merged data from both sources
    """
    # Load supplementary data from parquet file
    extra_df = pd.read_parquet(extra_data_path)
    
    # Merge main data with supplementary data
    merged_df = store_data.merge(extra_df, on="index")
    
    return merged_df
