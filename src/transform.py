import pandas as pd

def transform(raw_data):
    """
    Clean and transform raw data for analysis.
    
    Parameters:
    -----------
    raw_data : pandas.DataFrame
        Raw data from the extract step
        
    Returns:
    --------
    pandas.DataFrame
        Cleaned and transformed data
    """
    # Make a copy of the data to avoid modifying the original
    df = raw_data.copy()
    
    # Fill missing numerical values (NaN values) with the column mean
    numeric_cols = df.select_dtypes(include=['number']).columns
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].mean())
    
    # Add a "Month" column extracted from Date
    df['Month'] = pd.to_datetime(df['Date']).dt.month
    
    # Keep only rows where weekly sales are over $10,000
    df = df[df['Weekly_Sales'] > 10000]
    
    # Initialize list of columns to keep (excluding index)
    columns_to_keep = ['Store_ID', 'Dept', 'Weekly_Sales', 'Month']
    
    # Add additional columns if they exist in the dataframe
    if 'CPI' in df.columns:
        columns_to_keep.append('CPI')
    
    if 'Unemployment' in df.columns:
        columns_to_keep.append('Unemployment')
    
    # Make sure Date column is excluded
    if 'Date' in columns_to_keep:
        columns_to_keep.remove('Date')
    
    # Only keep the necessary columns
    df = df[columns_to_keep]
    
    return df

def avg_weekly_sales_per_month(clean_data):
    """
    Calculate average weekly sales per month.
    
    Parameters:
    -----------
    clean_data : pandas.DataFrame
        Cleaned data from the transform step
        
    Returns:
    --------
    pandas.DataFrame
        Aggregated monthly sales data
    """
    # Group by Month, calculate average Weekly_Sales
    result = clean_data.groupby('Month')['Weekly_Sales'].mean().reset_index()
    
    # Round results to two decimal places
    result['Weekly_Sales'] = round(result['Weekly_Sales'], 2)
    
    # Rename the column from Weekly_Sales to Avg_Sales
    result = result.rename(columns={'Weekly_Sales': 'Avg_Sales'})
    
    return result
