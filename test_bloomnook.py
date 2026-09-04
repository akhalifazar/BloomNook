# test_bloomnook.py
"""
Tests for BloomNook module.
"""

import unittest
from bloomnook import BloomNook

class TestBloomNook(unittest.TestCase):
    """Test cases for BloomNook class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BloomNook()
        self.assertIsInstance(instance, BloomNook)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BloomNook()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
