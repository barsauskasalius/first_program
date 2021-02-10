def find_needle(haystack):
    count = -1
    for i in haystack:
        count += 1
        if i == "needle":
            return f"found the needle at position {count}"
print(find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk']))
#https://www.codewars.com/kata/56676e8fabd2d1ff3000000c/train/python
def find_needle(haystack):
    index = haystack.index('needle')
    return 'found the needle at position {}'.format(index)