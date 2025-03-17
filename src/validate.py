import os
import pandas as pd

def validation(file_path):
    """
    Validate that an output file exists and contains valid data.
    
    Parameters:
    -----------
    file_path : str
        Path to the file to validate
        
    Returns:
    --------
    bool
        True if file exists and contains valid data, False otherwise
    """
    # Check if the file exists in the specified directory
    if not os.path.exists(file_path):
        return False
    
    # Try to read the CSV file to verify it's valid
    try:
        df = pd.read_csv(file_path)
        # Check if the file has content
        if df.empty:
            return False
        return True
    except Exception as e:
        print(f"Error validating {file_path}: {e}")
        return False
