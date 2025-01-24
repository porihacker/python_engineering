import unittest
from sum import add


class TestMathFunctions(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(add(4, 8), 12)
