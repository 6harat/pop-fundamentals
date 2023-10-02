def rp_mul(a: int, b: int):
    res = 0
    while b > 0:
        if b & 1 == 1:
            res += a
        a *= 2
        b //= 2
    return res


def rp_exp(num: int, pow: int):
    while pow & 1 == 0:
        num *= num
        pow //= 2
    res = num
    pow //= 2
    while pow > 0:
        num *= num
        if pow & 1 == 1:
            res *= num
        pow //= 2
    return res
