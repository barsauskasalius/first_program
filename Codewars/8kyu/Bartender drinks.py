param = input()
def get_drink_by_profession(param):
    if param.lower() == "jabroni":
        return "Patron Tequila"
    elif param.lower() == "school counselor":
        return "Anything with Alcohol"
    elif param.lower() == "programmer":
        return "Hipster Craft Beer"
    elif param.lower() == "bike gang member":
        return "Moonshine"
    elif param.lower() == "politician":
        return "Your tax dollars"
    elif param.lower() == "rapper":
        return "Cristal"
    else:
        return "Beer"
print(get_drink_by_profession(param))
#https://www.codewars.com/kata/568dc014440f03b13900001d/train/python