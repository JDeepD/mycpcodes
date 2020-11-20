# https://www.codewars.com/kata/55b7bb74a0256d4467000070

import math
from itertools import combinations
from operator import mul
from functools import reduce
def primeFactors(n):
    ls = []
    while n % 2 == 0:
        ls.append(2)
        n = n / 2
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            ls.append(i)
            n = n / i
    if n > 2:
        ls.append(n)
    return (ls)

def find_multiples(x,y,p):
    lw = math.floor(x/p) +1
    up = math.ceil(y/p) -1
    req = up-lw + 1
    return(req)

def proper_fractions(n):
    primes = list(set(primeFactors(n)))
    count = 0
    for i in primes:
        multiples = find_multiples(1, n, int(i))
        count += multiples
    tmp = 0
    for i in range(2, len(primes)+1):
        tmpls = list(combinations(primes, i))
        for j in tmpls:
            prod = reduce(mul, j, 1)
            multips = find_multiples(1, n, prod)
            tmp += multips*(-1)**i

    return n-count+tmp-1
