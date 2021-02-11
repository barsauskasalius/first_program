def paperwork(n, m):
    suma = n * m
    if n < 0 or m < 0:
        return 0
    else:
        return suma
#https://www.codewars.com/kata/55f9b48403f6b87a7c0000bd/train/python
def paperwork(n, m):
    return n * m if n > 0 and m > 0 else 0