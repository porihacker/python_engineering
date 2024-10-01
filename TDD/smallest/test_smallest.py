import unittest
from smallest import smallest

class TestSmallest(unittest.TestCase):
    def test_smallest(self):
        self.assertEqual(smallest([1, 2, 3]), 1)

    def test_smallest_negative(self):
        self.assertEqual(smallest([-1, -2, -3]), -3)