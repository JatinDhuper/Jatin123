#1. Write a function to find the sum of two numbers.

def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)


#2. Write a function to check whether a number is even or odd.

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd(7))


#3. Write a function to find the factorial of a number.

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

print("Factorial:", factorial(5))

#4. Write a function to find the maximum of two numbers.

def maximum(a, b):
    if a > b:
        return a
    else:
        return b

print("Maximum:", maximum(10, 20))


#5. Write a function to count vowels in a string.

def count_vowels(s):
    count = 0
    for ch in s:
        if ch in "aeiouAEIOU":
            count = count + 1
    return count

print("Vowels:", count_vowels("Python Programming"))



#6. Write a function to check whether a number is prime.

def is_prime(n):
    if n <= 1:
        return "Not Prime"
    for i in range(2, n):
        if n % i == 0:
            return "Not Prime"
    return "Prime"

print(is_prime(11))



#7. Write a function to reverse a string.

def reverse_string(s):
    return s[::-1]

print("Reversed String:", reverse_string("Python"))
