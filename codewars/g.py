# https://www.codewars.com/kata/51c8e37cee245da6b40000bd

def solution(string,markers):
    string = list(string)
    newline_pos = 0
    for i in string:
        if i in markers:
            temp = newline_pos + string.index(i)
            while temp < len(string) and string[temp] != '\n':
                temp += 1
            if string[string.index(i)-1] == ' ':
                del string[string.index(i)-1:temp]
            else:
                del string[string.index(i):temp]
    return ''.join(string)
