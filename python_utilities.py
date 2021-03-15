import copy
from collections import Counter

class Utilities():
    def __init__(self):
        print('Initialized!')

    @staticmethod
    def sum_list(my_list):
        return sum(my_list)

    @staticmethod
    def shallow_copy(my_list):
        return list(my_list)

    @staticmethod
    def deep_copy(my_list):
        return copy.deepcopy(my_list)

    @staticmethod
    def get_key_from_map_else_return_default(my_map, key):
        return my_map.get(key, 'Not Found')

    @staticmethod
    def get_key_from_map_else_return_default_ternary(my_map, key):
        return my_map[key] if key in my_map else 'Not Found'

    @staticmethod
    def sort_list_ascending(my_list):
        return sorted(my_list)

    @staticmethod
    def sort_list_descending(my_list):
        return sorted(my_list, reverse=True)
    
    @staticmethod
    def count_occurances_in_list(my_list, item):
        return my_list.count(item)
    
    @staticmethod
    def count_occurances_of_each_item_in_list(my_list):
        return Counter(my_list)
