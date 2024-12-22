import unittest
from algorithms import linear_search, binary_search

class TestSearchAlgorithms(unittest.TestCase):
    def setUp(self):
        self.test_array = [1, 3, 5, 7, 9, 11, 13, 15]
    
    def test_linear_search_found(self):
        self.assertEqual(linear_search(self.test_array, 7), 3)
        
    def test_linear_search_not_found(self):
        self.assertEqual(linear_search(self.test_array, 8), -1)
        
    def test_binary_search_found(self):
        self.assertEqual(binary_search(self.test_array, 11), 5)
        
    def test_binary_search_not_found(self):
        self.assertEqual(binary_search(self.test_array, 8), -1)
