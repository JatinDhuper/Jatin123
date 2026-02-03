#1. Write a program that prints the numbers from 1 to 50. For multiples of three, print "Fizz" instead of the number, and for the multiples of five, print "Buzz". For numbers which are multiples of both three and five, print "FizzBuzz":-

n2 = int(input("Enter a number from 1 to 100:"))
if n2%3==0 and n2%5==0:
    print("FizzBuzz")
elif n2%3==0:
    print("Fizz")
elif n2%5==0:
    print("Buzz")
else:
    print("Number is neither divisible by 3 nor by 5")


#2. Write a program to print all prime numbers between 1 and 100:-

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    # Check if n is divisible by 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False
    # Check for divisors from 5 onwards
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# List to store prime numbers
prime_numbers = []

# Iterate from 2 to 100
for number in range(2, 101):
    if is_prime(number):
        prime_numbers.append(number)

# Print the prime numbers
print("Prime numbers between 1 and 100 are:")
print(prime_numbers)



#3. Write a program that asks the user for a score between 0 and 100 and prints the corresponding grade. The grading scheme is:
"""90-100: A
80-89: B
70-79: C
60-69: D
Below 60: F"""

score = int(input("Enter a score between 0 and 100: "))

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"The corresponding grade for a score of {score} is: {grade}")


#4. Write a program that prints the multiplication table (from 1 to 10) for a given number

number = int(input("Enter a number to see its multiplication table: "))
print(f"Multiplication Table for {number}:")

# Use a for loop to iterate from 1 to 10
for i in range(1, 11):
    # Calculate the product
    product = number * i

    # Print the result in a clear format: number x i = product
    print(f"{number} x {i} = {product}")


#5. Write a program to create a list of the squares of the even numbers from 1 to 20.

squares_of_evens = []

for num in range(1, 21):
    # Check if the number is even
    if num % 2 == 0:
        # Calculate the square of the even number
        square = num ** 2
        # Add the square to the list
        squares_of_evens.append(square)

print(squares_of_evens)



#6. Write a program to check if a given year is a leap year. A year is a leap year if it is divisible by 4, but not by 100, unless it is also divisible by 400.

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")



#7. Write a program that takes the lengths of three sides of a triangle as input and determines the type of triangle (equilateral, isosceles,  scalene or right angle tringle ).

side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Check if the input lengths can form a valid triangle
# The sum of any two sides must be greater than the third side
if (side1 + side2 <= side3) or (side1 + side3 <= side2) or (side2 + side3 <= side1):
    print("The given side lengths do not form a valid triangle.")
else:
    # Check the type of triangle
    if side1 == side2 and side2 == side3:
        print("The triangle is Equilateral (all sides equal).")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("The triangle is Isosceles (two sides equal).")
    else:
        print("The triangle is Scalene (all sides different).")

    # Additionally, check if it's a right-angled triangle using the Pythagorean theorem (a^2 + b^2 = c^2)
    # Use a small tolerance for floating point comparisons
    tolerance = 0.001
    
    if abs(side1**2 + side2**2 - side3**2) < tolerance or \
       abs(side1**2 + side3**2 - side2**2) < tolerance or \
       abs(side2**2 + side3**2 - side1**2) < tolerance:
        print("The triangle is also a Right-angled triangle.")


#8. Write a program that takes an integer input from the user and classifies it as positive, negative, or zero.

number = int(input("Enter a number:"))

if number > 0:
    print(f"The number {number} is positive.")
elif number < 0:
    print(f"The number {number} is negative.")
else:
    print(f"The number {number} is zero.")


#10. Write a program that calculates the Body Mass Index (BMI) and categorizes it based on the following criteria:
"""BMI < 18.5: Underweight
   18.5 <= BMI < 24.9: Normal weight
   25 <= BMI < 29.9: Overweight
   BMI >= 30: Obesity"""

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("Category: Underweight")
elif 18.5 <= bmi < 25:
    print("Category: Normal weight")
elif 25 <= bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obesity")


#11. Write a program that takes an integer input representing a day of the week (1 for Monday, 2 for Tuesday, etc.) and prints the corresponding day name.

day_number = int(input("Enter a day number (1-7, where 1 is Monday): "))

if day_number == 1:
    print("Monday")
elif day_number == 2:
    print("Tuesday")
elif day_number == 3:
    print("Wednesday")
elif day_number == 4:
    print("Thursday")
elif day_number == 5:
    print("Friday")
elif day_number == 6:
    print("Saturday")
elif day_number == 7:
    print("Sunday")
else:
    print("Invalid input. Please enter a number between 1 and 7.")


#12. Write a program that calculates the discount on a product based on the following criteria:
"""If the price is greater than $1000, a discount of 10% is applied.
   If the price is between $500 and $1000, a discount of 5% is applied.
   If the price is below $500, no discount is applied."""

original_price = 1200.00 
discount_amount = 0.0

# Check if the price is greater than $1000
if original_price > 1000:
    discount_amount = original_price * 0.10
    
# Check if the price is between $500 and $1000 (inclusive of $500, exclusive of $1000 because of the first condition)
elif original_price >= 500:
    discount_amount = original_price * 0.05
    
# If neither of the above is true, the price is below $500, and no discount is applied
else:
    discount_amount = 0.0

# Calculate the final price
final_price = original_price - discount_amount

print(f"Original Price: ${original_price:.2f}")
print(f"Discount Applied: ${discount_amount:.2f}")
print(f"Final Price: ${final_price:.2f}")



#13. Write a program to find the sum of the first n natural numbers.

n = int(input("Enter a number: "))

# Using simple loop logic
sum = 0
for i in range(1, n+1):
    sum = sum + i

print("The sum of first", n, "natural numbers is:", sum)


#14. Given a dictionary employee_details where the keys are employee IDs and values are dictionaries with name, department, and salary, filter and create a list of names of employees who have a salary greater than 50,000.

employee_details = {
    101: {"name": "Alice", "department": "HR", "salary": 48000},
    102: {"name": "Bob", "department": "IT", "salary": 55000},
    103: {"name": "Charlie", "department": "Finance", "salary": 60000},
    104: {"name": "David", "department": "Marketing", "salary": 45000},
    105: {"name": "Eva", "department": "IT", "salary": 70000}
}

# Simple logic to filter employees
names = []
for emp_id in employee_details:
    if employee_details[emp_id]["salary"] > 50000:
        names.append(employee_details[emp_id]["name"])

print("Employees with salary greater than 50,000:", names)



#15. Write a program to count the number of vowels in a given string

text = input("Enter a string: ")

vowels = "aeiouAEIOU"   # All vowels (both lowercase and uppercase)
count = 0

for ch in text:
    if ch in vowels:
        count = count + 1

print("Number of vowels in the given string:", count)


#16. Write a program to find the sum of the digits of a given number.

#1st Method:-
num = int(input("Enter a number: "))
sum = 0

while num > 0:
    digit = num % 10      # Get the last digit
    sum = sum + digit     # Add it to sum
    num = num // 10       # Remove the last digit

print("Sum of digits is:", sum)

#2nd Method:-
num = input("Enter a number: ")
sum = 0

for ch in num:          # Loop through each character
    sum = sum + int(ch) # Convert character to integer and add

print("Sum of digits is:", sum)



#17. Write a program to print a pattern of stars. For example, if n = 5, the pattern should be
""" *
    **
    ***
    ****
    *****  """

n = int(input("Enter the number of rows: "))

for i in range(1, n+1):      # Loop from 1 to n
    print("*" * i)           # Print i stars


#18. Write a program for a number guessing game where the computer randomly selects a number between 1 and 100, and the user tries to guess it. The program should give hints if the guess is too high or too low.

import random

# Computer randomly selects a number between 1 and 100 
secret_number = random.randint(1, 100)

print("Guess the number between 1 and 100!")

# Loop until the user guesses correctly
while True:
    guess = int(input("Enter your guess: "))
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number correctly.")
        break


#19. Ask user to input a number and show all even number upto that number starting from number 1
"""Ex: 15
   2 4 6 8 10 12 14"""

n = int(input("Enter a number: "))

for i in range(2, n+1, 2):   # Start from 2, step by 2
    print(i, end=" ")


#20. WAP Create a list of 10 elements (Number elements) and perform the following
"""a. Tell element 25 exist or not
   b. Total length of List
   c. total occurrence of 25 in the list
   d. traverse of Each element
   e. Show All Even number in list"""

numbers = [10, 25, 30, 45, 25, 60, 75, 80, 25, 90]

# a. Tell element 25 exist or not
if 25 in numbers:
    print("Element 25 exists in the list.")
else:
    print("Element 25 does not exist in the list.")

# b. Total length of List
print("Total length of the list:", len(numbers))

# c. Total occurrence of 25 in the list
print("Total occurrence of 25:", numbers.count(25))

# d. Traverse each element
print("Traversing each element:")
for num in numbers:
    print(num, end=" ")
print()  # for new line

# e. Show all even numbers in the list
print("Even numbers in the list:")
for num in numbers:
    if num % 2 == 0:
        print(num, end=" ")


#21. Ask User to input a String of min 10 words and max 19 words and perform the following:
"""1. Print full string and length of string
   2. Tell String is palindrome or not mean
   3. Tell middle word in the string.
   4. Print Second last word in the String."""

text = input("Enter a string (min 10 words, max 19 words): ")
words = text.split()   # Split string into list of words

# 1. Print full string and length of string
print("Full string:", text)
print("Length of string:", len(text))

# 2. Tell if string is palindrome or not
# Palindrome means string reads same forward and backward
if text == text[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

# 3. Tell middle word in the string
middle_index = len(words) // 2
print("Middle word:", words[middle_index])

# 4. Print second last word in the string
print("Second last word:", words[-2])


#22. Perform the following Task as per the output
"""Welcome to Calci:
1. Power 
2. Sum
3. Sub
4. Multiple

Enter your choice. --> 2
Enter 1st Number for Sum: 100
Enter 2nd number for SUm: 200
Sum is 300"""

# Simple Calculator Program

print("Welcome to Calci:")
print("1. Power")
print("2. Sum")
print("3. Sub")
print("4. Multiple")

choice = int(input("Enter your choice. --> "))

if choice == 1:
    base = int(input("Enter base number: "))
    exp = int(input("Enter exponent number: "))
    result = base ** exp
    print("Power is", result)

elif choice == 2:
    num1 = int(input("Enter 1st Number for Sum: "))
    num2 = int(input("Enter 2nd Number for Sum: "))
    result = num1 + num2
    print("Sum is", result)

elif choice == 3:
    num1 = int(input("Enter 1st Number for Subtraction: "))
    num2 = int(input("Enter 2nd Number for Subtraction: "))
    result = num1 - num2
    print("Subtraction is", result)

elif choice == 4:
    num1 = int(input("Enter 1st Number for Multiplication: "))
    num2 = int(input("Enter 2nd Number for Multiplication: "))
    result = num1 * num2
    print("Multiplication is", result)

else:
    print("Invalid choice!")


#23. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same
# from a given list of strings.

"""Input :
   X = ['abc', 'xyz', 'aba', '1221']
   Output : 2"""

X = ['abc', 'xyz', 'aba', '1221']
count = 0

for s in X:
    if len(s) >= 2 and s[0] == s[-1]:
        count = count + 1

print("Output:", count)
