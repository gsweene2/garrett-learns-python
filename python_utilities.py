import copy

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