import unittest
import pandas as pd
import os
import tempfile
from src.load import load

class TestLoad(unittest.TestCase):
    
    def setUp(self):
        # Create sample data for testing
        self.clean_data = pd.DataFrame({
            'Store_ID': [1, 2, 3],
            'Dept': [1, 2, 3],
            'Weekly_Sales': [15000, 20000, 25000],
            'Month': [1, 1, 2]
        })
        
        self.agg_data = pd.DataFrame({
            'Month': [1, 2],
            'Avg_Sales': [17500, 25000]
        })
        
        # Create temporary directory for output files
        self.temp_dir = tempfile.TemporaryDirectory()
        self.clean_data_path = os.path.join(self.temp_dir.name, 'clean_data.csv')
        self.agg_data_path = os.path.join(self.temp_dir.name, 'agg_data.csv')
    
    def tearDown(self):
        # Clean up temporary files
        self.temp_dir.cleanup()
    
    def test_load_creates_files(self):
        # Call the load function
        result = load(self.clean_data, self.clean_data_path, 
                     self.agg_data, self.agg_data_path)
        
        # Check that the function returns True
        self.assertTrue(result)
        
        # Check that files were created
        self.assertTrue(os.path.exists(self.clean_data_path))
        self.assertTrue(os.path.exists(self.agg_data_path))
    
    def test_load_writes_correct_data(self):
        # Call the load function
        load(self.clean_data, self.clean_data_path, 
             self.agg_data, self.agg_data_path)
        
        # Read the files back
        clean_data_read = pd.read_csv(self.clean_data_path)
        agg_data_read = pd.read_csv(self.agg_data_path)
        
        # Check shapes
        self.assertEqual(clean_data_read.shape, self.clean_data.shape)
        self.assertEqual(agg_data_read.shape, self.agg_data.shape)
        
        # Check content
        pd.testing.assert_frame_equal(clean_data_read, self.clean_data)
        pd.testing.assert_frame_equal(agg_data_read, self.agg_data)

if __name__ == '__main__':
    unittest.main()
