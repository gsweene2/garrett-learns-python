import unittest

from python_utilities import Utilities

class TestPythonUtilities(unittest.TestCase):

    def test_sum(self):
        data = [1, 2, 3]
        result = Utilities.sum_list(data)
        self.assertEqual(result, 6)

    def test_shallow_copy(self):
        init_list = [1, 2, 3]
        copy_list = Utilities.shallow_copy(init_list)
        copy_list.append(4)
        self.assertEqual(init_list, [1, 2, 3])
        self.assertEqual(copy_list, [1, 2, 3, 4])

if __name__ == '__main__':
    unittest.main()
