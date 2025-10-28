# test_chainquery.py
"""
Tests for ChainQuery module.
"""

import unittest
from chainquery import ChainQuery

class TestChainQuery(unittest.TestCase):
    """Test cases for ChainQuery class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ChainQuery()
        self.assertIsInstance(instance, ChainQuery)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ChainQuery()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
