"""
solve all the math problems programmatically which can be found at:
    http://mathworld.wolfram.com
    https://www.hackerrank.com/contests/projecteuler/challenges
"""

def divisibility_by_3(num_string):
    """
    ref: https://www.geeksforgeeks.org/write-an-efficient-method-to-check-if-a-number-is-multiple-of-3/
    an alternative approach is implemented below which does not require recursion
    """
    fill_up = 0
    toggle_fill_up = lambda: (fill_up + int(2**(fill_up-1)))%3
    for i in num_string:
        i = int(i)
        fill_up = toggle_fill_up()
        fill_up = (fill_up - i)%3
    return fill_up == 0

def divisibility_by_k():
    """
    aka: deterministic_finite_automator, dfa
    ref: https://www.geeksforgeeks.org/dfa-based-division/
    """
    pass
    
def booth():
    """
    ref: https://www.geeksforgeeks.org/computer-organization-booths-algorithm/
    """
    pass