# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c

def duplicate_encode(word):
    ls = list(word.lower())
    dic = {}
    for i in ls:
        if i not in dic:
            dic[i] = True
        else:
            dic[i] = False

    for j, k in enumerate(ls):
        tmp = dic.get(k)
        if tmp:
            ls[j] = "("
        else:
            ls[j] = ")"
    return "".join(ls)
