def get_average(marks):
    suma = 0
    for vienas in marks:
        suma += vienas
    return int(suma / len(marks))


get_average([2, 4, 8])