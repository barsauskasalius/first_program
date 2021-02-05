## https://www.codewars.com/kata/58cb43f4256836ed95000f97/train/python
def find_difference(a, b):
    a = (a[0] * a[1] * a[2])
    b = (b[0] * b[1] * b[2])
    if b > a:
        return b - a
    else:
        return a - b