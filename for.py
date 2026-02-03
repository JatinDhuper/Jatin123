#1.Write a program to find the sum of first n natural numbers(n is integer input from user)
n = int(input("Enter an integer n:"))
sum = 0
# Check if n is a non-negative number
if n < 0:
    print("Please enter a positive integer.")
for i in range(0,n+1):
    sum += i

print("Sum of first", n, "natural numbers is:", sum)



#2. Print the multiplication table of a given number using a for loop
n1 = int(input("Enter an integer n:"))
print("Multiplication table of", n1, "is:")
for i in range(1, 11):
    # Calculate the product
    product = n1 * i
    # Print the result in a formatted string
    print(f"{n1} x {i} = {product}")


#3. write a program to check whether a given number is prime or not.
n= int(input("Enter number "))
print(n**0.5)
if n<=1:
    print("False")
else:
    prime= True
    for i in range(2,n):
        if n%i==0:
            prime=False
print(prime)

#4. Check whether a number is a palindrome.
#Eg: 1221
num = int(input("Enter a number: "))
original = num
rev = 0

# Count digits first
temp = num
count = 0
while temp > 0:
    temp //= 10
    count += 1

# Reverse using for loop
temp = num
for i in range(count):
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

# Check palindrome
if rev == original:
    print("Palindrome number")
else:
    print("Not a palindrome number")



#5. Print numbers from 1 to 100:
    # If number is divisible by 3 → print Fizz
    # If number is divisible by 5 → print Buzz
    # If number is divisible by both → print FizzBuzz

n2 = int(input("Enter a number from 1 to 100:"))
if n2%3==0 and n2%5==0:
    print("FizzBuzz")
elif n2%3==0:
    print("Fizz")
elif n2%5==0:
    print("Buzz")
else:
    print("Number is neither divisible by 3 nor by 5")