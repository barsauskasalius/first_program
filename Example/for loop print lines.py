numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ""  #info from second for loop that restars with empty string with each number
    for count in range(x_count): # Count all numbers from 0 to 5
        output += "x"
    print(f"{output}")