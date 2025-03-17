import unittest
import pandas as pd
import os
import tempfile
from src.validate import validation

class TestValidate(unittest.TestCase):
    
    def setUp(self):
        # Create temporary directory for test files
        self.temp_dir = tempfile.TemporaryDirectory()
        self.valid_file_path = os.path.join(self.temp_dir.name, 'valid.csv')
        self.empty_file_path = os.path.join(self.temp_dir.name, 'empty.csv')
        self.nonexistent_file_path = os.path.join(self.temp_dir.name, 'nonexistent.csv')
        
        # Create a valid CSV file
        valid_data = pd.DataFrame({
            'A': [1, 2, 3],
            'B': ['a', 'b', 'c']
        })
        valid_data.to_csv(self.valid_file_path, index=False)
        
        # Create an empty CSV file
        empty_data = pd.DataFrame()
        empty_data.to_csv(self.empty_file_path, index=False)
    
    def tearDown(self):
        # Clean up temporary files
        self.temp_dir.cleanup()
    
    def test_validation_valid_file(self):
        # Test validation of a valid file
        result = validation(self.valid_file_path)
        self.assertTrue(result)
    
    def test_validation_empty_file(self):
        # Test validation of an empty file
        result = validation(self.empty_file_path)
        self.assertFalse(result)
    
    def test_validation_nonexistent_file(self):
        # Test validation of a nonexistent file
        result = validation(self.nonexistent_file_path)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
