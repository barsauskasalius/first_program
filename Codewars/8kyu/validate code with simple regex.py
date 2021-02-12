def validate_code(code):
    strcode = int(str(code)[:1])
    if strcode <= 3:
        return True
    else:
        return False

print(validate_code(11))
#https://www.codewars.com/kata/56a25ba95df27b7743000016/train/python
def validate_code(code):
    return str(code).startswith(('1', '2', '3'))
def validate_code(code):
    return str(code)[0] in '123'