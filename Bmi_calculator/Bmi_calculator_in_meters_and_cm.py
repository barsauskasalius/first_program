print("Enter your weight in kg:")
weight = float(input())
print("Enter your height in meters or centimeters:")
height = input()
def bmi_calculator():
    if height[1] != ".":
        kmi: float = round((weight / float(height) ** 2) * 10000)
        return kmi
    else:
        kmi: float = round(weight / float(height) ** 2)
        return kmi
def compare():
    if kmi < 18.5:
        print("Underweight")
    elif 18.5 <= kmi < 25:
        print("Normal")
    elif 25 <= kmi < 30:
        print("Overweight")
    else:
        print("Obesity")
kmi = bmi_calculator()
print("Your kmi is:")
print(kmi)
compare()
