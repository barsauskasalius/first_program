def accum(s):
    lis = []
    count = 0
    for letter in s:
        letter = letter.lower()
        count += 1
        lis.append(letter*count)
    ats = [x.capitalize() for x in lis]
    return "-".join(ats)
print( accum("Abcd"))
#https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/solutions/python
def accum(s):
    output = ""
    for i in range(len(s)):
        output+=(s[i]*(i+1))+"-"
    return output.title()[:-1]