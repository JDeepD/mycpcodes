# https://www.codewars.com/kata/55a29405bc7d2efaff00007c



from math import factorial as fc
def going(n):
    res = 0
    for i in range(1, n+1):
        res += fac(i)
    x = res / fac(n)
    return truncate(x, 6)


cache = {}


def fac(n):
    if n in cache:
        return cache[n]
    if n == 0 or n==1:
        return 1
    if n >= 2:
        val = n*fac(n-1)
    cache[n] = val
    return val

import math
def truncate(number, digits):
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper
