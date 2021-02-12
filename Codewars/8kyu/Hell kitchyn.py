def square_sum(numbers):
    for i, x in enumerate(numbers):
        numbers[i] = sum(map(int, str(x)))

print(square_sum([0, 3, 4, 5]))
