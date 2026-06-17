# test_cryptoleap.py
"""
Tests for CryptoLeap module.
"""

import unittest
from cryptoleap import CryptoLeap

class TestCryptoLeap(unittest.TestCase):
    """Test cases for CryptoLeap class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoLeap()
        self.assertIsInstance(instance, CryptoLeap)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoLeap()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
