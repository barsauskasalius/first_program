def odd_or_even(arr):
    if sum(arr) % 2 == 0:
        return "even"
    return "odd"

print(odd_or_even([2, 1, 2]))
