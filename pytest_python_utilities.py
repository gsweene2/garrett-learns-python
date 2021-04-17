import copy
from collections import Counter, namedtuple


""" Argument Unpacking """


def unpack_dict_arguments(arg1, arg2, arg3):
    return {"arg1": arg1, "arg2": arg2, "arg3": arg3}


def test_unpack_dict_arguments():
    # Any order!
    arg_dict = {"arg2": "Argument 2", "arg1": "Argument 1", "arg3": "Argument 3"}
    result = unpack_dict_arguments(**arg_dict)
    expected = {"arg1": "Argument 1", "arg2": "Argument 2", "arg3": "Argument 3"}
    assert expected == result


""" Basic Comprehension """


def string_to_list_comprehension(my_string):
    letter_list = [letter for letter in my_string]
    return letter_list


""" Test Basic Comprehension """


def test_string_to_list_comprehension():
    # Arrange
    my_string = "awesome"
    # Act
    result_string = string_to_list_comprehension(my_string)
    # Assert
    expected = ["a", "w", "e", "s", "o", "m", "e"]
    assert expected == result_string


""" Caesar Cipher single Character (Unicode)"""


def caesar_cipher_single_character(character, number):
    # Get unicode decimal
    uni = ord(character)
    # Add number to create new unicode decimal
    new_uni = uni + number
    # Since A-z are 96-122, check to see if still in range
    if new_uni <= 122:
        return chr(new_uni)
    return chr((new_uni + 96) % 122)


""" Test Caesar Cipher single Character """


def test_caesar_cipher_single_character():
    # Arrange
    character, number = "a", 1
    # Act
    result = caesar_cipher_single_character(character, number)
    # Assert
    assert "b" == result


def test_caesar_cipher_single_character():
    # Arrange
    character, number = "z", 1
    # Act
    result = caesar_cipher_single_character(character, number)
    # Assert
    assert "a" == result


""" Collections: namedtuples """


def create_golf_hole_named_tuple(hole_number, par):
    Hole = namedtuple("hole", "number par")
    return Hole(hole_number, par)


""" Test Collections: namedtuples """


def test_create_golf_hole_named_tuple():
    # Arrange
    hole_number = 18
    par = 4
    # Act
    hole_tuple = create_golf_hole_named_tuple(hole_number, par)
    # Assert
    assert 18 == hole_tuple.number
    assert 4 == hole_tuple.par


""" Count Occurances in List """


def count_occurances_in_list(my_list, item):
    return my_list.count(item)


def count_occurances_of_each_item_in_list(my_list):
    return Counter(my_list)


""" Test Count Occurances in List """


def test_count_occurances_in_list():
    # Arrange
    my_list = [1, 3, 4, 2, 2, 2, 4, 2]
    # Act
    occurances = count_occurances_in_list(my_list, 2)
    # Assert
    assert 4 == occurances


def test_count_occurances_of_each_item_in_list():
    # Arrange
    my_list = ["a", "c", "d", "b", "b", "b", "c", "b"]
    # Act
    occurances = count_occurances_of_each_item_in_list(my_list)
    # Assert
    expected = {"a": 1, "b": 4, "c": 2, "d": 1}
    assert expected == occurances


""" Deep and Shallow Copy """


def shallow_copy(my_list):
    return list(my_list)


def deep_copy(my_list):
    return copy.deepcopy(my_list)


""" Test Deep and Shallow Copy """


def test_shallow_copy__modify_object_in_init_list__should_affect_copy_list():
    # Arrange
    init_list = [1, 2, 3, [1, 2, 3]]
    # Act
    copy_list = shallow_copy(init_list)
    init_list[3].append(4)
    # Assert
    assert copy_list == [1, 2, 3, [1, 2, 3, 4]]
    assert init_list == [1, 2, 3, [1, 2, 3, 4]]


def test_deep_copy__modify_object_in_init_list__should_not_affect_copy_list():
    # Arrange
    init_list = [1, 2, 3, [1, 2, 3]]
    # Act
    copy_list = deep_copy(init_list)
    init_list[3].append(4)
    # Assert
    assert copy_list == [1, 2, 3, [1, 2, 3]]
    assert init_list == [1, 2, 3, [1, 2, 3, 4]]


""" Find Substrings in list of Strings with Comprehensions """


def find_strings_that_contain_substring_in_list_comprehension(
    list_of_strings, substring
):
    return [word for word in list_of_strings if substring in word.lower()]


""" Test Find Substrings in list of Strings with Comprehensions """


def test_find_strings_that_contain_substring_in_list_comprehension():
    # Arrange
    list_of_strings = ["Fred", "Freedy", "Reddison", "Dave", "Bob", "Red"]
    # Act
    result = find_strings_that_contain_substring_in_list_comprehension(
        list_of_strings, "red"
    )
    # Assert
    expected = ["Fred", "Reddison", "Red"]
    assert expected == result


""" Get key from map """


def get_key_from_map_else_return_default(my_map, key):
    return my_map.get(key, "Not Found")


def get_key_from_map_else_return_default_ternary(my_map, key):
    return my_map[key] if key in my_map else "Not Found"


""" Test Get key from map """


def test_get_key_from_map_else_return_default_key_exists():
    # Arrange
    my_map = {"a": 1, "b": 2, "c": 3}
    # Act
    value = get_key_from_map_else_return_default(my_map, "a")
    # Assert
    assert value == 1


def test_get_key_from_map_else_return_default_key_dne():
    # Arrange
    my_map = {"a": 1, "b": 2, "c": 3}
    # Act
    value = get_key_from_map_else_return_default(my_map, "z")
    # Assert
    assert value == "Not Found"


def test_get_key_from_map_else_return_default_ternary_key_exists():
    # Arrange
    my_map = {"a": 1, "b": 2, "c": 3}
    # Act
    value = get_key_from_map_else_return_default_ternary(my_map, "a")
    # Assert
    assert value == 1


def test_get_key_from_map_else_return_default_ternary_key_dne():
    # Arrange
    my_map = {"a": 1, "b": 2, "c": 3}
    # Act
    value = get_key_from_map_else_return_default_ternary(my_map, "z")
    # Assert
    assert value == "Not Found"


""" Lambda welcome message """

print_welcome_lambda = lambda first, last: f"Welcome to garretts-docs, {first} {last}"

""" Test Lambda welcome message """


def test_print_welcome_lambda():
    # Arrage
    first, last = "Garrett", "Smith"
    # Act
    result = print_welcome_lambda(first, last)
    # Assert
    expected = "Welcome to garretts-docs, Garrett Smith"
    assert expected == result


""" Merge Dictionaries """


def merge_dictionaries(dict_1, dict_2):
    return {**dict_1, **dict_2}


""" Test Merge Dictionaries """


def test_merge_dictionaries():
    # Arrage
    older_data = {"bob": 35, "phil": 39, "katie": 30}
    newer_data = {"phil": 41, "fred": 19}
    # Act
    result = merge_dictionaries(older_data, newer_data)
    # Assert
    expected = {"bob": 35, "phil": 41, "katie": 30, "fred": 19}
    assert expected == result


def test_merge_dictionaries():
    # Arrage
    older_data = {"phil": 41, "fred": 19}
    newer_data = {"bob": 35, "phil": 39, "katie": 30}
    # Act
    result = merge_dictionaries(older_data, newer_data)
    # Assert
    expected = {"phil": 39, "fred": 19, "bob": 35, "katie": 30}
    assert expected == result


""" Sorting """


def sort_list_ascending(my_list):
    return sorted(my_list)


def sort_list_descending(my_list):
    return sorted(my_list, reverse=True)


def sort_dictionary_on_value(my_dict):
    return sorted(my_dict.items(), key=lambda x: x[1], reverse=True)


""" Test Sorting """


def test_sort_list_ascending__should_return_sorted_list():
    # Arrange
    my_list = ["A", "C", "D", "B", "E"]
    # Act
    sorted_list = sort_list_ascending(my_list)
    # Assert
    expected = ["A", "B", "C", "D", "E"]
    assert sorted_list == expected


def test_sort_list_descending__should_return_sorted_list():
    # Arrange
    my_list = ["A", "C", "D", "B", "E"]
    # Act
    sorted_list = sort_list_descending(my_list)
    # Assert
    expected = ["E", "D", "C", "B", "A"]
    assert sorted_list == expected


def test_sort_dictionary_on_value():
    # Arragne
    my_dict = {"bob": 97, "fred": 67, "katie": 78, "sophie": 99}
    # Act
    sorted_list = sort_dictionary_on_value(my_dict)
    # Assert
    expected_list = [("sophie", 99), ("bob", 97), ("katie", 78), ("fred", 67)]
    assert expected_list == sorted_list


""" Sum """


def sum_list(my_list):
    return sum(my_list)


""" Test Sum """


def test_sum():
    # Arrange
    data = [1, 2, 3]
    # Act
    result = sum_list(data)
    # Assert
    assert result == 6


def test_sum():
    # Arrange
    data = [1, 2, 3]
    # Act
    result = sum_list(data)
    # Assert
    assert result, 6
