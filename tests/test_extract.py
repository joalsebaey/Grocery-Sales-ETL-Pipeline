import unittest
import pandas as pd
import os
import tempfile
from src.extract import extract

class TestExtract(unittest.TestCase):
    
    def setUp(self):
        # Create sample data for testing
        self.store_data = pd.DataFrame({
            'index': [1, 2, 3],
            'Store_ID': [1, 2, 3],
            'Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
            'Weekly_Sales': [15000, 20000, 12000]
        })
        
        # Create temporary parquet file with extra data
        self.temp_dir = tempfile.TemporaryDirectory()
        self.extra_data_path = os.path.join(self.temp_dir.name, 'extra_data.parquet')
        
        extra_data = pd.DataFrame({
            'index': [1, 2, 3],
            'CPI': [200.1, 200.2, 200.3],
            'Unemployment': [5.1, 5.2, 5.3]
        })
        extra_data.to_parquet(self.extra_data_path)
        
    def tearDown(self):
        # Clean up temporary files
        self.temp_dir.cleanup()
    
    def test_extract_merges_data_correctly(self):
        # Call the extract function
        result = extract(self.store_data, self.extra_data_path)
        
        # Check that result has correct shape
        self.assertEqual(result.shape, (3, 6))
        
        # Check that all columns from both sources are present
        expected_columns = ['index', 'Store_ID', 'Date', 'Weekly_Sales', 'CPI', 'Unemployment']
        self.assertListEqual(sorted(result.columns.tolist()), sorted(expected_columns))
        
        # Check that values were merged correctly
        self.assertEqual(result.loc[0, 'Store_ID'], 1)
        self.assertEqual(result.loc[0, 'CPI'], 200.1)

if __name__ == '__main__':
    unittest.main()
