#1. Word Frequenct with Sortinng:- 
# Write a python program that takes a sentence as input and stores word frequencies in a dictionary. 
# Finally, print the dictionary sorted by frquency in descending order.

sentence = input("Enter a sentence: ")

# Initialize an empty dictionary to store word frequencies
word_counts = {}
cleaned_sentence = sentence.lower()
temp_words = ""
for char in cleaned_sentence:
    if 'a' <= char <= 'z' or '0' <= char <= '9' or char == ' ':
        temp_words += char
    else:
        temp_words += ' ' # replace other characters with a space

# Split the cleaned string into a list of words, handling multiple spaces
words = [word for word in temp_words.split() if word]

# Count the frequency of each word
for word in words:
    # If the word is already a key in the dictionary, increment its count
    if word in word_counts:
        word_counts[word] += 1
    # Otherwise, add the word to the dictionary with a count of 1
    else:
        word_counts[word] = 1

# Convert the dictionary to a list of (word, frequency) tuples
# This is necessary for sorting by value (frequency)
items_list = list(word_counts.items())

# Sort the list of tuples by frequency in descending order
# The 'key' argument uses a 'lambda' function to specify that the second element of each tuple (the frequency) should be used for sorting.
# 'reverse=True' sorts in descending order.
items_list.sort(key=lambda item: item[1], reverse=True)

print("\nWord frequencies sorted by frequency (descending):")
for word, count in items_list:
    print(f"'{word}': {count}")



#2. Student GradeReport:-
# Create a dictionary with student names as keys and their marks as values.
# Write a program that:
# Calculate the average marks
# Prints names of students scoring above average.

student_marks = {
    "Alice": 88,
    "Bob": 72,
    "Charlie": 95,
    "David": 65,
    "Eve": 81
}

total_marks = 0
num_students = 0

# Iterate through the dictionary to sum marks and count students
for marks in student_marks.values():
    total_marks += marks
    num_students += 1

average_marks = total_marks / num_students

print(f"Student Marks: {student_marks}")
print(f"Total Marks: {total_marks}")
print(f"Number of Students: {num_students}")
print(f"Average Marks: {average_marks:.2f}\n") # Formatting to 2 decimal places

print("Students scoring above average:")

# Iterate through the dictionary again to check each student's marks against the average
for name, marks in student_marks.items():
    if marks > average_marks:
        print(name)


#3. Combine Dictionaries with Conditions:-
# Given two dictionarirs, merge them such that:
# • If a key exists in both dictionaries, keep the maximum value
# • Otherwise, keep the original key-value pair

dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 25, 'c': 5, 'd': 40}

merged_dict = dict1.copy()

for key, value in dict2.items():
    if key in merged_dict:
        # Key exists in both, keep the maximum value
        if value > merged_dict[key]:
            merged_dict[key] = value
    else:
        # Key is only in dict2, add it to the merged dictionary
        merged_dict[key] = value

print(merged_dict)


#4. Find Key with Maximum Length Value:-
# Given a dictionary where values are strings, write a program to find the key whose value has the maximum length.


my_dict = {
    'a': 'apple',
    'b': 'banana',
    'c': 'kiwi',
    'd': 'dragonfruit'
}

max_len = -1
max_key = None


for key, value in my_dict.items():
    #Check the length of current value
    if len(value) > max_len:
        max_len = len(value)
        max_key = key

print("Key:", max_key)
print("Value:", my_dict[max_key])
print("Length:", max_len)


#5. Filter Dictionary by Value Range:-
#Write a Python program to filter a dictionary and create a new dictionary containing only those
#key–value pairs where the value lies between 10 and 50 (inclusive).

original_dict = {
    'item1': 5,
    'item2': 15,
    'item3': 60,
    'item4': 30,
    'item5': 45,
    'item6': 90
}

filtered_dict = {}

for key, value in original_dict.items():
    if 10 <= value <= 50:
        filtered_dict[key] = value

print("Original dictionary:", original_dict)
print("Filtered dictionary (values between 10 and 50, inclusive):", filtered_dict)


#6.Dictionary-Based Voting System:-
"""Create a dictionary to store votes for candidates.
   Write a program that:
    ● Accepts votes as input
    ● Counts votes using a dictionary
    ● Displays the winner (candidate with maximum votes)"""

votes = {}   # empty dictionary to store votes
n = int(input("Enter number of voters: "))

for i in range(n):
    name = input("Enter candidate name: ")

    if name in votes:
        votes[name] = votes[name] + 1
    else:
        votes[name] = 1

# finding winner
max_votes = 0
winner = ""

for name in votes:
    if votes[name] > max_votes:
        max_votes = votes[name]
        winner = name

print("Votes:", votes)
print("Winner:", winner)
print("Votes received:", max_votes)



#7. Replace Values Using Another Dictionary
"""Given two dictionaries:
    ● The first dictionary contains keys and values
    ● The second dictionary contains replacement values
    Write a program to replace values of the first dictionary only if the key exists in the second dictionary."""

dict1 = {
    "a": 10,
    "b": 20,
    "c": 30,
    "d": 40
}

dict2 = {
    "b": 200,
    "d": 400,
    "e": 500
}

for key in dict1:
    if key in dict2:
        dict1[key] = dict2[key]

print("Updated Dictionary:")
print(dict1)
