def flip(d, a):
    if d == "R":
        a.sort()
    elif d == "L":
        a.sort(reverse=True)
    return a
print(flip('L', [1, 4, 5, 3, 5]))
#https://www.codewars.com/kata/5f70c883e10f9e0001c89673/train/python