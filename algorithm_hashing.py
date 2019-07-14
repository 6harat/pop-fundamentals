"""
ref: https://www.youtube.com/watch?v=z0lJ2k0sl1g
     https://www.youtube.com/watch?v=0M_kIqhwbFo
tricks for hashing a string:
    - ((n*a + b)*n + c) can be computed faster than (a*n^2 + b*n + c)
    - use % at each step to prevent overflowing the int capacity
    - use the closest power of 2 such as 32 instead of 27 (num_letters)
      to enable use of bitwise operators
"""


def universal_hashing(object):
    """
    ref: 
    """
    pass


def perfect_hashing(object):
    """
    ref: 
    """
    pass


def consistent_hashing(object):
    """
    ref: https://en.wikipedia.org/wiki/Consistent_hashing
         https://www.toptal.com/big-data/consistent-hashing
    """
    pass


def rendezvous_hashing(object):
    """
    ref: https://en.wikipedia.org/wiki/Rendezvous_hashing
    """
    pass
