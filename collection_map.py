"""
load_factor, L = num_elements/map_size
"""

class Probing(object):
    @staticmethod
    def linear():
        """
        probe_length, P = (1 + 1/((1-L)**2))/2      :for successful search
                        = (1 + 1/(1-L))/2           :for unsuccessful search
        load_factor must be kept < 2/3 (or less than 1/2) for adequately short probe_lengths
        """
        pass

    @staticmethod
    def quadratic():
        """
        probe_length, P = -log2(1 - L)/L            :for successful search
                        = 1/(1-L)                   :for unsuccessful search
        load_factor must be kept < 0.8 (or less than 2/3) for adequately short probe_lengths
        """
        pass

    @staticmethod
    def rehashed():
        pass

class OpenAddressingHashMap(object):
    """
    all elements are stored in the hash map itself. 
    i.e. collisions are resolved by finding the next open cell through a procedure called probing
    for modulus-based-hash, the map_size should be a prime number.
    this enable all elements to get discovered unlike for the case of non-prime number
    where the indices may start to repeat and the program ends up in an endless loop
    """
    def __init__(self, size, probe=Probing.linear):
        pass

class SeparateChainingHashMap(object):
    """
    each entry in map points to a linked_list/tree.
    all elmenets with the same hash_value are stored in the corresponding linked_list/tree
    load_factor can increase beyond 1 without hurting the performance much.
    considered as a robust choice espectially when the num_elements are unknown/unpredictable.
    it is not mandatory to keep the map_size as a prime numbers
    search_time, S = 1 + L/2                        :for successful search (irrespective of order)
                   = 1 + L                          :for unsuccessful search (unorderd_list)
                   = 1 + L/2                        :for unsuccessful search (ordered_list)
    load_factor is usually maintained as 1 due to the linear dependency between L and S
    """
    pass

class TreeMap(object):
    pass

class MultiMap(object):
    pass

class LinkedHashMap(object):
    pass