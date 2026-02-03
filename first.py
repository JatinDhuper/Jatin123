#1. Printing Names using print function 
name = input("Enter your name:")
print("The name you entered is:", name)


print("-----------------------------------------------------")
#2. Simple Calculator

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
op = input("Enter the operation you want to perform:")

if op =="addition":
    print("Addition of two number=", a+b)
if op =="subtraction":
    print("Subtraction of two number=", a-b)
if op =="product":
    print("Multiplication of two number=", a*b)
if op =="division":
    try:
        print("Division of two number=", a/b)
    except Exception as e:
        print("Zero Division Error",  e)
        


print("-----------------------------------------------------")
#3. To check number is even or odd
num = int(input("Enter the number:"))
if num %2 == 0:
    print("The number is even")
else:
    print("The number is odd")


print("-----------------------------------------------------")
#4. To check if a person is eligible to vote or not
# Prompt the user for age input
age = int(input("Enter your age: "))

# Check if the age is 18 or older
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


print("-----------------------------------------------------")
#5. To check if a number is positive, negative or zero
# Assign a value to a variable (or use input() for user interaction)
number = int(input("Enter the number:"))

# Check the conditions sequentially
if number > 0:
    print(f"The number {number} is positive.")
elif number < 0:
    print(f"The number {number} is negative.")
else:
    print(f"The number {number} is zero.")
