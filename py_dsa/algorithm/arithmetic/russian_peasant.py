def is_odd(num: int):
    return num & 1 == 1

def rp_mul(a: int, b: int):
    res = 0
    while b > 0:
        if is_odd(b):
            res += a
        a *= 2
        b //= 2
    return res


def rp_exp(num: int, pow: int):
    while not is_odd(pow):
        num *= num
        pow //= 2
    res = num
    pow //= 2
    while pow > 0:
        num *= num
        if is_odd(pow):
            res *= num
        pow //= 2
    return res
