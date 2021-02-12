def max_redigit(num):
    str_num = str(num)
    if  len(str_num)==3 and num > 0:
        num_list = list(map(int, str(num)))

        num_list.sort(reverse=True)

        strings = [str(integer) for integer in num_list]
        a_string = "".join(strings)
        an_integer = int(a_string)
        return an_integer
    else:
        return None

#https://www.codewars.com/kata/563700da1ac8be8f1e0000dc/train/python