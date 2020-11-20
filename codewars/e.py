# https://www.codewars.com/kata/5552101f47fc5178b1000050

def dig_pow(n, p):
    b = n
    n = list(map(int, str(n)))
    sum_ = 0

    for digit, power in zip(n, range(p, len(n)+1 + p)):
        sum_ += digit**power
    if sum_ % b == 0 and sum_ != 0:
        return sum_/b
    else:
        return -1
