def bmi_calculator():
    print("Enter your weight in kg:")
    weight = float(input())
    print("Enter your height in meters:")
    height = float(input())
    kmi = round(weight / height**2)
    if kmi < 18.5:
      print("Underweight")
    elif 18.5 <= kmi and kmi < 25:
      print("Normal")
    elif kmi >= 25 and kmi < 30:
      print("Overweight")
    else:
      print("Obesity")
bmi_calculator()
