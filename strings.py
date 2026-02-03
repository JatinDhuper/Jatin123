#1. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return ‘not a valid string’ instead of the empty string
"""Sample string: - “Coder roots”
Expected result - “cots”
Sample string - “New year”
Expected result - “near”"""


input_string = input("Enter a String:")
string_length = len(input_string)

if string_length < 2:
    result_string = 'not a valid string'
    
else:
    # If yes, extract the first 2 characters
    first_two = input_string[0:2]
    # Extract the last 2 characters
    last_two = input_string[-2:]
    # Combine them to form the result string
    result_string = first_two + last_two

print(f"Original string: '{input_string}'")
print(f"Resulting string: '{result_string}'")


#2. Write a Python program to get a single string from two given strings, separated by a space and swap the first characters of each string
"""Sample String : 'coder', 'roots'
Expected Result : 'roder coots'"""

string1 = input("Enter First String:")
string2 = input("Enter Second String:")

print(f"Original string 1: {string1}")
print(f"Original string 2: {string2}")


new_string1 = string2[0] + string1[1:]

new_string2 = string1[0] + string2[1:]

# Combine the new strings with a space separator
result_string = new_string1 + ' ' + new_string2

# Display the resulting string
print(f"\nResult after swapping first characters and joining: {result_string}")


#3. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged
"""Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'"""

string1 = input("Enter a String:")

length = len(string1)
result = ""

if length < 3:
    result = string1
elif string1.endswith('ing'):
    result = string1 + 'ly'
else:
    result = string1 + 'ing'

print(f"Original string: {string1}")
print(f"Modified string: {result}")


#4. Write a Python program to remove the nth index character from a nonempty string

original_string = input("Enter a String:")
n = int(input("Enter the index of character you want to remove:"))

# Check if the string is empty:-
if not original_string:
    print("Error: The string is empty.")
else:
    first_part = original_string[:n]
    second_part = original_string[n+1:]
    
    # Combine the two parts to create the new string
    new_string = first_part + second_part
    
    print("Original string:", original_string)
    print(f"String after removing the character at index {n}:", new_string)

