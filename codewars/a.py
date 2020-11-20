# https://www.codewars.com/kata/58efb6ef0849132bf000008f


def build_palindrome(s):
    ls = list(s)
    i = 0
    while ls != ls[::-1]:
        ls.insert(i, ls[-1-i])
        i += 1
    pk = list(s)
    k = len(pk)
    p = 0
    while pk != pk[::-1] and p < k:
        pk.insert(k, pk[p])
        p += 1
    if len(pk) > len(ls):
        return "".join(ls)
    else:
        return "".join(pk)
