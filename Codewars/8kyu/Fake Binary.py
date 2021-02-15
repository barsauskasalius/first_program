def fake_bin(x):
    ats = []
    for element in x:
        if int(element)<5:
            ats.append("0")
        else:
            ats.append("1")
    return "".join(ats)
#https://www.codewars.com/kata/57eae65a4321032ce000002d/train/python

print(fake_bin("0555011110001100111"))
