#1. Write a Python function average_marks that accepts any number of integer marks using *args.
"""The function should:
    1. Ignore any mark that is less than 0
    2. Return the average of the remaining marks
    3. If no valid marks are provided, return 0"""

def average_marks(*marks):
    total = 0
    count = 0

    for m in marks:
        if m >= 0:
            total = total + m
            count = count + 1

    if count == 0:
        return 0
    else:
        return total / count

print(average_marks(50, 80, -10, 70))   # Output: 66.66666666666667
print(average_marks(-5, -10))          # Output: 0
print(average_marks(90, 85, 95))       # Output: 90.0



#2. Write a Python function filter_details that accepts any number of keyword arguments using **kwargs.
"""The function should:
    1. Print only those key–value pairs where the value is a string
    2. Print them in the format: key = value"""

def filter_details(**details):
    for key, value in details.items():
        if type(value) == str:
            print(key, "=", value)

filter_details(
    name="Jatin",
    age=20,
    city="Delhi",
    marks=85,
    course="Python"
)
