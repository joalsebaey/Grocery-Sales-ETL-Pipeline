import unittest
import pandas as pd
import numpy as np
from src.transform import transform, avg_weekly_sales_per_month

class TestTransform(unittest.TestCase):
    
    def setUp(self):
        # Create sample data for testing
        self.raw_data = pd.DataFrame({
            'Store_ID': [1, 2, 3, 4, 5],
            'Dept': [1, 2, 1, 2, 3],
            'Date': ['2023-01-15', '2023-01-22', '2023-02-15', '2023-02-22', '2023-03-15'],
            'Weekly_Sales': [15000, 20000, 8000, 12000, 25000],
            'CPI': [200.1, 200.2, np.nan, 200.4, 200.5],
            'Unemployment': [5.1, 5.2, 5.3, np.nan, 5.5]
        })
    
    def test_transform_handles_missing_values(self):
        result = transform(self.raw_data)
        
        # Check that NaN values were filled
        self.assertFalse(result['CPI'].isna().any())
        self.assertFalse(result['Unemployment'].isna().any())
    
    def test_transform_filters_low_sales(self):
        result = transform(self.raw_data)
        
        # Check that rows with sales <= 10000 were removed
        self.assertEqual(len(result), 3)
        self.assertTrue((result['Weekly_Sales'] > 10000).all())
    
    def test_transform_creates_month_column(self):
        result = transform(self.raw_data)
        
        # Check that Month column was created correctly
        self.assertIn('Month', result.columns)
        self.assertEqual(set(result['Month'].unique()), {1, 2, 3})
    
    def test_transform_selects_correct_columns(self):
        result = transform(self.raw_data)
        
        # Check that output has the correct columns
        expected_columns = ['Store_ID', 'Dept', 'Weekly_Sales', 'Month', 'CPI', 'Unemployment']
        self.assertListEqual(sorted(result.columns.tolist()), sorted(expected_columns))
        
        # Check that Date column was removed
        self.assertNotIn('Date', result.columns)
    
    def test_avg_weekly_sales_per_month(self):
        # First transform the data
        clean_data = transform(self.raw_data)
        
        # Calculate aggregates
        result = avg_weekly_sales_per_month(clean_data)
        
        # Check structure
        self.assertEqual(result.shape[0], 3)  # 3 months
        self.assertEqual(result.shape[1], 2)  # Month and Avg_Sales columns
        
        # Check column renaming
        self.assertIn('Avg_Sales', result.columns)
        self.assertNotIn('Weekly_Sales', result.columns)

if __name__ == '__main__':
    unittest.main()
