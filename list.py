#1. Create a list with 5 friends and ask user a friend name and
"""Add that name in the friend list,
   And print the list
   After that ask user to most important friend and add that friend at user choice"""

# Ex: [1,2,3,4,5]
# -> Enter another friend: Raju
# [1,2,3,4,5,"Raju"]
# --> Most important friend: Billa
# --> Please select the location for billa: 1
#   [1,"Billa",3,4,5,"Raju"]


friend_list = ["Alice", "Bob", "Charlie", "David", "Eve"]

print("Initial friend list:", friend_list)
new_friend = input("Enter another friend's name: ")
friend_list.append(new_friend)

print("List after adding the new friend:", friend_list)
important_friend = input("Who is your most important friend? ")


try:
    location = int(input(f"Please select the location for {important_friend}: "))
    friend_list.insert(location - 1, important_friend)

    print("Final list after adding the most important friend at the chosen location:", friend_list)

except ValueError:
    print("Invalid input for location. Please enter a number next time.")
except IndexError:
    print("Location index is out of range.")


#2. Create a list of 10 number and print the list


numbers_list = []

# Loop 10 times to take 10 numbers as input from the user
for i in range(10):
    while True:
        try:
            user_input = input(f"Enter number {i + 1} of 10: ")
            
            # Convert the input to a floating-point number (allows for integers or decimals)
            number = float(user_input)
            
            # Add the valid number to the list
            numbers_list.append(number)
            
            # Break the inner while loop once valid input is received
            break 
            
        except ValueError:
            # Handle cases where the user input is not a valid number
            print("Invalid input. Please enter a numerical value.")

# Print a separator for clarity
print("-" * 20)

# Print the final list of numbers
print("The list of 10 numbers is:")
print(numbers_list)



#3. Create a list [1,10,100,3,6,8] and add 59 on 3 location after that append 5 and print list and length of list

my_list = [1, 10, 100, 3, 6, 8]

# Add 59 on the 3rd location (index 3)
my_list.insert(3, 59)
# Append 5 to the end of the list
my_list.append(5)

# Print the list and its length
print("Updated list:", my_list)
print("Length of the list:", len(my_list))


#4. Find all of the words in a list of strings that are less than 4 letters

li1 = ["Hello this is the test", "On a summer day", "in the sun"]

# Filter words with length less than 4
short_words = [word for sentence in li1 for word in sentence.split() if len(word) < 4]
print("Required List:")
print(short_words)


#5. Given numbers = range(20), produce a list containing the word ‘even’ if a number in the numbers is even, and the word ‘odd’ if the number is odd. Result would look like ‘odd’,'even',........ 

numbers = range(20)
result_list = ['even' if num % 2 == 0 else 'odd' for num in numbers]
print("Requireed List:")
print(result_list)


#6. Find all of the numbers from 1-1000 that are divisible by 7 

li2 = [number for number in range(1, 1001) if number % 7 == 0]
print("Required List of numbers from 1-1000 which ar divisible by 7:")
print(li2)


#7. Count the number of spaces in a string 

#1st Method(With List):-
my_string = "Count the spaces in this sentence"

# Convert the string to a list of characters
char_list = list(my_string)

# Use the list.count() method to count spaces
space_count = char_list.count(' ')

# Print the result
print(f"The string is: '{my_string}'")
print(f"The number of spaces using a list is: {space_count}")


#2nd Method(With String):-
text = "This is a sample string with spaces"
space_count = text.count(' ')
print(space_count)

#3rd Method:-
my_string = "Count the number of spaces in this string."
space_count = sum(1 for char in my_string if char == ' ')
print(f"The number of spaces is: {space_count}")


#8. Find the common numbers in two lists (without using a tuple or set) list_a = 1, 2, 3, 4, list_b = 2, 3, 4, 5

list_a = [1, 34, 22, 5, 10, 2]
list_b = [2, 23, 5, 11, 67, 34]

print("First List:", list_a)
print("Second List:", list_b)

common_numbers = [item for item in list_a if item in list_b]
common_numbers = []
for item in list_a:
    if item in list_b:
        common_numbers.append(item)
print("List having common numbers among two lists:", common_numbers)
