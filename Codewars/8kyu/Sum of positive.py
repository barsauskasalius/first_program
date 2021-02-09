def positive_sum(arr):
    visas = [x for x in arr if x > -x]
    return sum(visas)
print(positive_sum([1,-4,7,12]))
#https://www.codewars.com/kata/5715eaedb436cf5606000381/train/python
def postive_sum(arr):
    sum = 0
    for e in arr:
        if e > 0:
            sum = sum + e
    return sum