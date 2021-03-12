import unittest

from python_utilities import Utilities

class TestSum(unittest.TestCase):

    def test_sum(self):
        data = [1, 2, 3]
        result = Utilities.sum_list(data)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()
