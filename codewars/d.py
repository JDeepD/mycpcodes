# https://www.codewars.com/kata/520b9d2ad5c005041100000f

def pig_it(text):
    text = text.split()
    ls = []
    for wd in text:
        l = list(wd)
        l.append(l[0])
        del l[0]
        wd = "".join(l)
        if wd[-1].isalpha():
            wd += 'ay'
        ls.append(wd)
        ls.append(" ")
    return ''.join(ls).strip()
