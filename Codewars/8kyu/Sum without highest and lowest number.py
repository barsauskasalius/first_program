def sum_array(arr):
        if arr is None or len(arr) <= 1:
            return 0
        else:
            return sum(sorted(arr)[1:-1])

print(sum_array([6, 2, 1, 8, 10]))

#https://www.codewars.com/kata/576b93db1129fcf2200001e6/train/python
