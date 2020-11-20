# https://www.codewars.com/kata/5254ca2719453dcc0b00027d


import itertools


def permutations(string):
    st = list(string)
    number = list(range(len(string)))
    alliters = list(itertools.permutations(number))
    stdout = []
    for iteration in alliters:
        temp = []
        for letterindex in iteration:
            temp.append(st[letterindex])
        stdout.append(''.join(temp))
    return set(stdout)
