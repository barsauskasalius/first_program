def first_non_consecutive(arr):
    for index, numb in enumerate(arr):
        next_numb = numb + 1
        if len(arr) - 1 == index:
            return None
        if next_numb != arr[index + 1]:
            return arr[index + 1]

result = first_non_consecutive([4, 5, 6, 7, 8, 9, 11])



