# https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39


ls = []

def zero(*args): #your code here
    ls.append("0")
    if len(ls) >= 3:
        x = eval(''.join(ls[::-1]))
        ls.clear()
        return x
def one(*args): #your code here
    ls.append("1")
    if len(ls) >= 3:
        x = eval(''.join(ls[::-1]))
        ls.clear()
        return x
def two(*args): #your code here
    ls.append("2")
    if len(ls) >= 3:
        x = eval(''.join(ls[::-1]))
        ls.clear()
        return x
def three(*args): #your code here
    ls.append("3")
    if len(ls) >= 3:
        x = eval(''.join(ls[::-1]))
        ls.clear()
        return x
def four(*args): #your code here
    ls.append("4")
    if len(ls) >= 3:
        x = eval(''.join(ls[::-1]))
        ls.clear()
        return x
def five(*args): #your code here
    ls.append("5")
    if len(ls) >= 3:
        x = eval(''.join(ls[::-1]))
        ls.clear()
        return x
def six(*args): #your code here
    ls.append("6")
    if len(ls) >= 3:
        x = eval(''.join(ls[::-1]))
        ls.clear()
        return x
def seven(*args): #your code here
    ls.append("7")
    if len(ls) >= 3:
        x = eval(''.join(ls[::-1]))
        ls.clear()
        return x
def eight(*args): #your code here
    ls.append("8")
    if len(ls) >= 3:
        x = eval(''.join(ls[::-1]))
        ls.clear()
        return x
def nine(*args): #your code here
    ls.append("9")
    if len(ls) >= 3:
        x = eval(''.join(ls[::-1]))
        ls.clear()
        return x

def plus(*args): #your code here
    ls.append("+")
    pass
def minus(*args): #your code here
    ls.append("-")
def times(*args): #your code here
    pass
    ls.append("*")
def divided_by(*args): #your code here
    pass
    ls.append("//")

