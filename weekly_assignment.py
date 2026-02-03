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


#4. Write a program that prints the multiplication table (from 1 to 10) for a given number

#5. Write a program to create a list of the squares of the even numbers from 1 to 20.



#6. Write a program to check if a given year is a leap year. A year is a leap year if it is divisible by 4, but not by 100, unless it is also divisible by 400.



#7. Write a program that takes the lengths of three sides of a triangle as input and determines the type of triangle (equilateral, isosceles,  scalene or right angle tringle ).


#8. Write a program that takes an integer input from the user and classifies it as positive, negative, or zero.


#10. Write a program that calculates the Body Mass Index (BMI) and categorizes it based on the following criteria:
BMI < 18.5: Underweight
18.5 <= BMI < 24.9: Normal weight
25 <= BMI < 29.9: Overweight
BMI >= 30: Obesity
11. 

#11. Write a program that takes an integer input representing a day of the week (1 for Monday, 2 for Tuesday, etc.) and prints the corresponding day name.


#12. Write a program that calculates the discount on a product based on the following criteria:
"""If the price is greater than $1000, a discount of 10% is applied.
If the price is between $500 and $1000, a discount of 5% is applied.
If the price is below $500, no discount is applied."""


13. Write a program to find the sum of the first n natural numbers.

14. Given a dictionary employee_details where the keys are employee IDs and values are dictionaries with name, department, and salary, filter and create a list of names of employees who have a salary greater than 50,000.

15. Write a program to count the number of vowels in a given string

16. Write a program to find the sum of the digits of a given number.

17. Write a program to print a pattern of stars. For example, if n = 5, the pattern should be
*
**
***
****
*****

18. Write a program for a number guessing game where the computer randomly selects a number between 1 and 100, and the user tries to guess it. The program should give hints if the guess is too high or too low.

19. 
Ask user to input a number and show all even number upto that number starting from number 1
Ex: 15
2 4 6 8 10 12 14

20.
WAP Create a list of 10 elements (Number elements) and perform the following
a. Tell element 25 exist or not
b. Total length of List
c. total occurrence of 25 in the list
d. traverse of Each element
e. Show All Even number in list

21.
Ask User to input a String of min 10 words and max 19 words and perform the following:
1. Print full string and length of string
2. Tell String is palindrome or not mean
3. Tell middle word in the string.
4. Print Second last word in the String.

22.
Perform the following Task as per the output

Welcome to Calci:
1. Power 
2. Sum
3. Sub
4. Multiple

Enter your choice. --> 2
Enter 1st Number for Sum: 100
Enter 2nd number for SUm: 200
Sum is 300

23.
Write a Python program to count the number of strings where the
string length is 2 or more and the first and last character are same
from a given list of strings.

Input :
X = ['abc', 'xyz', 'aba', '1221']
Output : 2
