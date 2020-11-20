# https://www.codewars.com/kata/52a89c2ea8ddc5547a000863


def loop_size(node):
    start = 0
    turtle, hare = node, node
    while (turtle.next and hare.next.next):
        if turtle == hare and start != 0:
            count = 0
            turtle = turtle.next
            while turtle != hare:
                count += 1
                turtle = turtle.next
            return count+1
        turtle = turtle.next
        hare = hare.next.next
        start = 1
    return
