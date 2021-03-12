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

    def test_shallow_copy__modify_copied_non_object__should_not_affect_init_list(self):
        # Arrange
        init_list = [1, 2, 3, [1, 2, 3]]
        # Act
        copy_list = Utilities.shallow_copy(init_list)
        copy_list.append(4)
        # Assert
        self.assertEqual(copy_list, [1, 2, 3, [1, 2, 3], 4])
        self.assertEqual(init_list, [1, 2, 3, [1, 2, 3]])

    def test_shallow_copy__modify_init_non_object__should_not_affect_copy_list(self):
        # Arrange
        init_list = [1, 2, 3, [1, 2, 3]]
        # Act
        copy_list = Utilities.shallow_copy(init_list)
        init_list.append(4)
        # Assert
        self.assertEqual(copy_list, [1, 2, 3, [1, 2, 3]])
        self.assertEqual(init_list, [1, 2, 3, [1, 2, 3], 4])

    def test_shallow_copy__modify_object_in_init_list__should_affect_copy_list(self):
        # Arrange
        init_list = [1, 2, 3, [1, 2, 3]]
        # Act
        copy_list = Utilities.shallow_copy(init_list)
        init_list[3].append(4)
        # Assert
        self.assertEqual(copy_list, [1, 2, 3, [1, 2, 3, 4]])
        self.assertEqual(init_list, [1, 2, 3, [1, 2, 3, 4]])

    def test_deep_copy__modify_copied_non_object__should_not_affect_init_list(self):
        # Arrange
        init_list = [1, 2, 3, [1, 2, 3]]
        # Act
        copy_list = Utilities.deep_copy(init_list)
        copy_list.append(4)
        # Assert
        self.assertEqual(copy_list, [1, 2, 3, [1, 2, 3], 4])
        self.assertEqual(init_list, [1, 2, 3, [1, 2, 3]])

    def test_deep_copy__modify_init_non_object__should_not_affect_copy_list(self):
        # Arrange
        init_list = [1, 2, 3, [1, 2, 3]]
        # Act
        copy_list = Utilities.deep_copy(init_list)
        init_list.append(4)
        # Assert
        self.assertEqual(copy_list, [1, 2, 3, [1, 2, 3]])
        self.assertEqual(init_list, [1, 2, 3, [1, 2, 3], 4])

    def test_deep_copy__modify_object_in_init_list__should_not_affect_copy_list(self):
        # Arrange
        init_list = [1, 2, 3, [1, 2, 3]]
        # Act
        copy_list = Utilities.deep_copy(init_list)
        init_list[3].append(4)
        # Assert
        self.assertEqual(copy_list, [1, 2, 3, [1, 2, 3]])
        self.assertEqual(init_list, [1, 2, 3, [1, 2, 3, 4]])

    def test_get_key_from_map_else_return_default_key_exists(self):
        # Arrange
        my_map = {'a':1,'b':2,'c':3}
        # Act
        value = Utilities.get_key_from_map_else_return_default(my_map, 'a')
        # Assert
        self.assertEqual(value, 1)

    def test_get_key_from_map_else_return_default_key_dne(self):
        # Arrange
        my_map = {'a':1,'b':2,'c':3}
        # Act
        value = Utilities.get_key_from_map_else_return_default(my_map, 'z')
        # Assert
        self.assertEqual(value, 'Not Found')


    def test_get_key_from_map_else_return_default_ternary_key_exists(self):
        # Arrange
        my_map = {'a':1,'b':2,'c':3}
        # Act
        value = Utilities.get_key_from_map_else_return_default_ternary(my_map, 'a')
        # Assert
        self.assertEqual(value, 1)

    def test_get_key_from_map_else_return_default_ternary_key_dne(self):
        # Arrange
        my_map = {'a':1,'b':2,'c':3}
        # Act
        value = Utilities.get_key_from_map_else_return_default_ternary(my_map, 'z')
        # Assert
        self.assertEqual(value, 'Not Found')

    def sort_list_ascending__should_return_sorted_list(self):
        # Arrange
        my_list = ['A','C','D','B','E']
        # Act
        sorted_list = Utilities.sort_list_ascending(my_list)
        # Assert
        expected = ['A','B','C','D','E']
        self.assertEqual(sorted_list,expected)

    def sort_list_descending__should_return_sorted_list(self):
        # Arrange
        my_list = ['A','C','D','B','E']
        # Act
        sorted_list = Utilities.sort_list_descending(my_list)
        # Assert
        expected = ['E','D','C','B','A']
        self.assertEqual(sorted_list,expected)

if __name__ == '__main__':
    unittest.main()
