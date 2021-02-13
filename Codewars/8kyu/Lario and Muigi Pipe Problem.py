def pipe_fix(nums):
    list = []
    for i in range(nums[0], nums[-1]+1):
        list.append(i)
    return list


print(pipe_fix([1, 3, 5, 6, 7, 8]))
