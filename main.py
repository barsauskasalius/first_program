def bonus_time(salary, bonus):
    if bonus:
        return "$" + str(salary * 10)
    return "$" + str(salary)



grazint = bonus_time(1000, True)
bonus_time(5000, False)
ok = bonus_time(-10, True)

print(ok)