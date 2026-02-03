#Question 1
"""WAP Ask user to input a number and then month name corresponding to that number"""

month_number = int(input("Enter a number between 1 and 12: "))
if month_number == 1:
    print("The month corresponding to the number 1 is January.")
elif month_number == 2:
    print("The month corresponding to the number 2 is February.")
elif month_number == 3:
    print("The month corresponding to the number 3 is March.")
elif month_number == 4:
    print("The month corresponding to the number 4 is April.")
elif month_number == 5:
    print("The month corresponding to the number 5 is May.")
elif month_number == 6:
    print("The month corresponding to the number 6 is June.")
elif month_number == 7:
    print("The month corresponding to the number 7 is July.")
elif month_number == 8:
    print("The month corresponding to the number 8 is August.")
elif month_number == 9:
    print("The month corresponding to the number 9 is September.")
elif month_number == 10:
    print("The month corresponding to the number 10 is October.")
elif month_number == 11:
    print("The month corresponding to the number 11 is November.")
elif month_number == 12:
    print("The month corresponding to the number 12 is December.")
else:
    print("Invalid input: Please enter a number between 1 and 12.")


#Question 2
#WAP Ask user to input 2 number,
#Tell the following:
#1. Both number are equal or not
#2. Which is Bigger in both
#3. Either First NUmber is smaller or equal to Second Number
#4. Print your first name 5 times if first number is greather than second ,and print your surname 3 times if 1st no is less than second

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

#Checking if both numbers are equal or not
if a==b:
    print("Both numbers are equal")
else:
    print("Both numbers are not equal")

#Checking which number is bigger
if a<b:
    print("a is bigger than b")
else:
    print("b is bigger than a")

#Checking Either First NUmber is smaller or equal to Second Number
if a<=b:
    print("a is smaller or equal to b")
else:
    print("a is not smaller or equall to b(b is bigger than a)")

# Print your first name 5 times if first number is greather than second ,and print your surname 3 times if 1st no is less than second
name = input("Enter your Full name:")
words = name.split(" ")
print(words)
first_name = words[0]
sur_name = words[1]
if a>b:
    for i in range (5):
        print(first_name)

elif a<b:
    for i in range(3):
        print(sur_name)



#Question 3:
"""Using User input ask user to input 2 string and tell followings
1. using == tell both string equal or not
2. using is operator tell both equal or not"""

str1 = input("Enter first String:")
str2 = input("Enter second String:")
#Checking if both strings are equal or not:
"""The major difference between the == and is operators in Python is that 
   == checks for value equality 
   while is checks for identity (whether two variables refer to the exact same object in memory)"""

f1= str1 == str2
f2= str1 is str2
if f1 == True:
    print("Values of both string is equal")
else:
    print("Value Equality is not met")

if f2 == True:
    print("Identity of both strings is equal")
else:
    print("Identity of both strings is not equal")


#Question 4:
"""Ask user to input 2 string and convert it into numbers and using is op
tell both are equal or not"""


s1 = input("Enter first numeric string: ")
s2 = input("Enter second numeric string: ")

"""
'Hello' is not a number, so Python cannot convert it to int
 int() works only with numeric strings like "10", "25", etc.
"""

n1 = int(s1)
n2 = int(s2)

if n1 is n2:
    print("Both numbers are equal")
else:
    print("Both numbers are not equal")


#Question5"
# Python program to calculate the sum of all numbers from 1 to a given number.

num = int(input("Enter the number upto which you  want to find sum of all numbers:"))
for i in range (0, num):
    


#Question6:
"""
Ask user to input a number and tell all even number upto that number
Eg:
input a num:29
Even are:
2,4,6,... 28"""

#Question7: Ask User to input a Number and with + or - and perform followings Output
"""Enter a no: 567
   Enter OP(+,-): +
   0,1,2,3.......566
   if -
   567...>..... 1"""
