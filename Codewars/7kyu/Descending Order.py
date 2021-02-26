import math


def descending_order(num):
    res = [int(x) for x in str(num)]
    res.sort()
    res.reverse()
    strings = [str(integer) for integer in res]
    a_string = "".join(strings)
    an_integer = int(a_string)
    return an_integer

def descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))
print(descending_Order(123456789))