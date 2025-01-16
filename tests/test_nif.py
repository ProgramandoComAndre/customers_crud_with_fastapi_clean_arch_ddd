import sys
import os
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from features.customers.value_objects import Nif

class NifTest(unittest.TestCase):
    def test_should_validate_nif(self):
        value = "272714224"
        result = Nif(value)
        self.assertIsInstance(result, Nif, "Valid Nif")
    def test_should_not_validate_nif_if_characters_are_different_of_nine(self):
        value = "2"
        self.assertRaises(ValueError, lambda: Nif(value))
    def test_should_not_validate_nif_if_invalid(self):
        value = "999999999"
        self.assertRaises(ValueError, lambda: Nif(value))



if __name__=="__main__":
    unittest.main()