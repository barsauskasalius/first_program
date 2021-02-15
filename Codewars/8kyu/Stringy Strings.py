def stringy(size):
    ats = ""
    for num in range(0,size):
        if num%2 == 0:
            ats += "1"
        else:
            ats += "0"
    return ats
print(stringy(4))

#https://www.codewars.com/kata/563b74ddd19a3ad462000054/train/python