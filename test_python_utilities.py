import unittest

from python_utilities import Utilities

class TestPythonUtilities(unittest.TestCase):

    def test_sum(self):
        # Arrange
        data = [1, 2, 3]
        # Act
        result = Utilities.sum_list(data)
        # Assert
        self.assertEqual(result, 6)

    def test_shallow_copy_modify_copied(self):
        # Arrange
        init_list = [1, 2, 3]
        # Act
        copy_list = Utilities.shallow_copy(init_list)
        copy_list.append(4)
        # Assert
        self.assertEqual(init_list, [1, 2, 3])
        self.assertEqual(copy_list, [1, 2, 3, 4])

    def test_shallow_copy_modify_init(self):
        # Arrange
        init_list = [1, 2, 3]
        # Act
        copy_list = Utilities.shallow_copy(init_list)
        init_list.append(4)
        # Assert
        self.assertEqual(copy_list, [1, 2, 3])
        self.assertEqual(init_list, [1, 2, 3, 4])

    def test_deep_copy_modify_copied(self):
        # Arrange
        init_list = [1, 2, 3]
        # Act
        copy_list = Utilities.deep_copy(init_list)
        copy_list.append(4)
        # Assert
        self.assertEqual(copy_list, [1, 2, 3, 4])
        self.assertEqual(init_list, [1, 2, 3])

    def test_deep_copy_modify_init(self):
        # Arrange
        init_list = [1, 2, 3]
        # Act
        copy_list = Utilities.deep_copy(init_list)
        init_list.append(4)
        # Assert
        self.assertEqual(copy_list, [1, 2, 3])
        self.assertEqual(init_list, [1, 2, 3, 4])

if __name__ == '__main__':
    unittest.main()
