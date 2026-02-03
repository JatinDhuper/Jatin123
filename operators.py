#1. Write a python program that takes in a student name, class, and section. It should also take in five subject marks of the students and find the total mark and percentage. Display a result in such a way that their name, class, section, and percentage are printed.

name = input("Enter the Student's Name:")
classs = input("Enter the Student's Class:")
section = input("Enter the Student's section:")

mark1 = int(input("Enter the marks in Subject 1:"))
mark2 = int(input("Enter the marks in Subject 2:"))
mark3 = int(input("Enter the marks in Subject 3:"))
mark4 = int(input("Enter the marks in Subject 4:"))
mark5 = int(input("Enter the marks in Subject 5:"))

print("Required student is ", name)
print(name, "studies in ", classs)
print("The Section in which", name, "reads is ", section)

obtained_marks = mark1 + mark2 + mark3 + mark4 + mark5
print("Total Marks in 5 Subjects=", obtained_marks)
percentage = (obtained_marks/500) * 100
print("Percentage Marks=", percentage)


#2. Input 3 numbers and return sum of them.
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

summ = a + b + c
print("The Sum of 3 numbers is:", summ)

#3 .Input a number and return square of it.
a = int(input("Enter the number you want to get square of:"))
square = a**2
print("The square of ", a, ":", square)


#4. Write a program to:
# Take the temperature in Celsius as input (string format).
# Convert it into a float.
# Calculate the equivalent temperature in Fahrenheit using the formula: Fahrenheit=(Celsius×9/5​)+32
# Print the result in both Celsius and Fahrenheit.

temp =  input("Enter the temperature in Celsius:")
temp1 = float(temp)
Fahrenheit = (temp1*(9/5)) + 32
print("Required temperature in Celsius:", temp1)
print("Required temperature in Fahrenheit:", Fahrenheit)


#5. Write a program to calculate the remainder when a number is divided by another number.
# Input: Two integers from the user.
# Output: Quotient and remainder.
a = int(input("Enter Numerator:"))
b = int(input("Enter Denominator:"))
remainder = a%b
quotient = a//b
print("Quotient when",a, "is divided by", b,":", quotient )
print("Remainder when",a, "is divided by", b,":", remainder)


#6. Write a program to calculate using the formula:
# SI = (P × R × T) / 100
# where P = Principal, R = Rate, T = Time.

P = int(input("Enter Principal Amount:"))
R = int(input("Enter Rate of Interest:"))
T = int(input("Enter Time Period:"))

SI = (P* R*T) / 100

print("Simple Interest=", SI)

