def longest(a1, a2):
    new_string = set(a1+a2)
    list_string = list(new_string)
    list_string.sort()
    ans_string = "".join(list_string)
    return ans_string