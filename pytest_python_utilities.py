from python_utilities import Utilities

def test_sum():
    # Arrange
    data = [1, 2, 3]
    # Act
    result = Utilities().sum_list(data)
    # Assert
    assert result == 6

def test_sum():
    # Arrange
    data = [1, 2, 3]
    # Act
    result = Utilities.sum_list(data)
    # Assert
    assert result, 6

def test_shallow_copy__modify_copied_non_object__should_not_affect_init_list():
    # Arrange
    init_list = [1, 2, 3, [1, 2, 3]]
    # Act
    copy_list = Utilities.shallow_copy(init_list)
    copy_list.append(4)
    # Assert
    assert copy_list == [1, 2, 3, [1, 2, 3], 4]
    assert init_list == [1, 2, 3, [1, 2, 3]]

def test_shallow_copy__modify_init_non_object__should_not_affect_copy_list():
    # Arrange
    init_list = [1, 2, 3, [1, 2, 3]]
    # Act
    copy_list = Utilities.shallow_copy(init_list)
    init_list.append(4)
    # Assert
    assert copy_list == [1, 2, 3, [1, 2, 3]]
    assert init_list == [1, 2, 3, [1, 2, 3], 4]

def test_shallow_copy__modify_object_in_init_list__should_affect_copy_list():
    # Arrange
    init_list = [1, 2, 3, [1, 2, 3]]
    # Act
    copy_list = Utilities.shallow_copy(init_list)
    init_list[3].append(4)
    # Assert
    assert copy_list == [1, 2, 3, [1, 2, 3, 4]]
    assert init_list == [1, 2, 3, [1, 2, 3, 4]]

def test_deep_copy__modify_copied_non_object__should_not_affect_init_list():
    # Arrange
    init_list = [1, 2, 3, [1, 2, 3]]
    # Act
    copy_list = Utilities.deep_copy(init_list)
    copy_list.append(4)
    # Assert
    assert copy_list == [1, 2, 3, [1, 2, 3], 4]
    assert init_list == [1, 2, 3, [1, 2, 3]]

def test_deep_copy__modify_init_non_object__should_not_affect_copy_list():
    # Arrange
    init_list = [1, 2, 3, [1, 2, 3]]
    # Act
    copy_list = Utilities.deep_copy(init_list)
    init_list.append(4)
    # Assert
    assert copy_list == [1, 2, 3, [1, 2, 3]]
    assert init_list == [1, 2, 3, [1, 2, 3], 4]

def test_deep_copy__modify_object_in_init_list__should_not_affect_copy_list():
    # Arrange
    init_list = [1, 2, 3, [1, 2, 3]]
    # Act
    copy_list = Utilities.deep_copy(init_list)
    init_list[3].append(4)
    # Assert
    assert copy_list == [1, 2, 3, [1, 2, 3]]
    assert init_list == [1, 2, 3, [1, 2, 3, 4]]

def test_get_key_from_map_else_return_default_key_exists():
    # Arrange
    my_map = {'a':1,'b':2,'c':3}
    # Act
    value = Utilities.get_key_from_map_else_return_default(my_map, 'a')
    # Assert
    assert value == 1

def test_get_key_from_map_else_return_default_key_dne():
    # Arrange
    my_map = {'a':1,'b':2,'c':3}
    # Act
    value = Utilities.get_key_from_map_else_return_default(my_map, 'z')
    # Assert
    assert value == 'Not Found'


def test_get_key_from_map_else_return_default_ternary_key_exists():
    # Arrange
    my_map = {'a':1,'b':2,'c':3}
    # Act
    value = Utilities.get_key_from_map_else_return_default_ternary(my_map, 'a')
    # Assert
    assert value == 1

def test_get_key_from_map_else_return_default_ternary_key_dne():
    # Arrange
    my_map = {'a':1,'b':2,'c':3}
    # Act
    value = Utilities.get_key_from_map_else_return_default_ternary(my_map, 'z')
    # Assert
    assert value == 'Not Found'

def test_sort_list_ascending__should_return_sorted_list():
    # Arrange
    my_list = ['A','C','D','B','E']
    # Act
    sorted_list = Utilities.sort_list_ascending(my_list)
    # Assert
    expected = ['A','B','C','D','E']
    assert sorted_list == expected

def test_sort_list_descending__should_return_sorted_list():
    # Arrange
    my_list = ['A','C','D','B','E']
    # Act
    sorted_list = Utilities.sort_list_descending(my_list)
    # Assert
    expected = ['E','D','C','B','A']
    assert sorted_list == expected

def test_count_occurances_in_list():
    # Arrange
    my_list = [1, 3, 4, 2, 2, 2, 4, 2]
    # Act
    occurances = Utilities.count_occurances_in_list(my_list, 2)
    # Assert
    assert 4 == occurances
