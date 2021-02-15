st = 'Print only the words that start with s in this sentence'
kitas = st.split()
lis = []
for word in kitas:
    if word[0] == "s":
        lis.append(word)

print (lis)

#Use range() to print all the even numbers from 0 to 10.
ats = []
for x in range(1, 11):
    if x % 2 == 0:
        ats.append(x)

print(ats)
#Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
lis = []
for num in range(1,50):
        lis.append(num * 3)
print(lis[:16])
#Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
lis = st.split()
count = []
for x in lis:
    if len(x) % 2 == 0:
        count.append(x)
stringa = " ".join(count)
print(count)
#Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
for x in range(1,101):
    if x%3 and x%5 == 0:
        print("FizzBuzz")
        continue
    elif x%3 == 0:
        print("Fizz")
        continue
    elif x%5 == 0:
        print("Buzz")
        continue
    else:
        print(x)
#Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
lis = st.split()
nums = []
for x in lis:
    nums.append(x[0][0])
print(nums)
