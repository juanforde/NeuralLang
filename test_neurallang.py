# test_neurallang.py
"""
Tests for NeuralLang module.
"""

import unittest
from neurallang import NeuralLang

class TestNeuralLang(unittest.TestCase):
    """Test cases for NeuralLang class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NeuralLang()
        self.assertIsInstance(instance, NeuralLang)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NeuralLang()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
