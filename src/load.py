def load(full_data, full_data_file_path, agg_data, agg_data_file_path):
    """
    Save processed data to output files.
    
    Parameters:
    -----------
    full_data : pandas.DataFrame
        Cleaned and transformed data
    full_data_file_path : str
        Path where cleaned data should be saved
    agg_data : pandas.DataFrame
        Aggregated data
    agg_data_file_path : str
        Path where aggregated data should be saved
        
    Returns:
    --------
    bool
        True if operation was successful
    """
    # Save the full cleaned data to CSV without index
    full_data.to_csv(full_data_file_path, index=False)
    
    # Save the aggregated data to CSV without index
    agg_data.to_csv(agg_data_file_path, index=False)
    
    return True
