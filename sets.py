#Question 1: The Guest List
"""You have two sets of names representing guests for Friday and Saturday.
friday = {"Alice", "Bob", "Charlie"}
saturday = {"Charlie", "David", "Eve"}
• Task: Create a new set called all_guests that contains everyone attending at least one night.
• Task: Identify the guest who is attending both nights."""

friday = {"Alice", "Bob", "Charlie"}
saturday = {"Charlie", "David", "Eve"}

# Task 1: Create a new set called all_guests (Union)
all_guests = friday | saturday
print("All guests:", all_guests)

# Task 2: Identify the guest attending both nights (Intersection)
both_nights = friday & saturday
print("Attending both nights:", both_nights)


#Question 2: List Cleaner
"""You have a list with duplicates: data = [1, 2, 2, 3, 4, 4, 4, 5].
• Task: Convert this list into a set to remove duplicates, then add the number 6 to that set."""

data = [1, 2, 2, 3, 4, 4, 4, 5]

unique_data_set = set(data)
unique_data_set.add(6)

print("Required Set:-")
print(unique_data_set)


#3. Question 3: The Library Audit
"""You have a set of all books owned by a library and a set of books currently checked out.
library_books = {"Hobbit", "1984", "Gatsby", "Odyssey", "Hamlet"}
checked_out = {"1984", "Hamlet"}
• Task: Use a set operation to find the books currently sitting on the shelf (available).
• Task: A student brings a "Don Quixote" to donate. Check if this book is not already in the
library_books before adding it."""

library_books = {"Hobbit", "1984", "Gatsby", "Odyssey", "Hamlet"}
checked_out = {"1984", "Hamlet"}

# Task 1: Find books currently on the shelf (Difference operation)
available_books = library_books - checked_out
print("Books available on the shelf:", available_books)

# Task 2: Check and add a donated book
new_book = "Don Quixote"
if new_book not in library_books:
    library_books.add(new_book)
    print(f"Added '{new_book}' to the library.")
else:
    print(f"'{new_book}' is already in the library inventory.")

print("Updated library collection:", library_books)



#4. Question 4: Permission Checker
"""A user has user_permissions = {"read", "write"}. The admin requirements for a folder are
admin_reqs = {"read", "write", "execute"}.
• Task: Use a method to check if the user has all the permissions required for admin access (Is
the user's set a subset of the requirements?).
• Task: Find the specific permissions the user is missing."""

user_permissions = {"read", "write"}
admin_reqs = {"read", "write", "execute"}

# 1.Check if the user has all required permissions (Is the user's set a subset of the requirements?)
#   Use the issubset() method or the '<=' operator
has_all_permissions_subset_method = admin_reqs.issubset(user_permissions)
has_all_permissions_operator = admin_reqs <= user_permissions  # Alternative using the operator

print(f"User permissions: {user_permissions}")
print(f"Admin requirements: {admin_reqs}")
print(f"Does the user have all required admin permissions? {has_all_permissions_subset_method}")

# 2. Find the specific permissions the user is missing
missing_permissions_method = admin_reqs.difference(user_permissions)
missing_permissions_operator = admin_reqs - user_permissions   #Alternative method
print(f"Permissions the user is missing: {missing_permissions_operator}")



#5. Question 5: The Log Analyzer
"""You are given a dictionary where the keys are "Error Codes" and the values are lists of "Server IDs"
where those errors occurred.
Python
logs = {
"404": [10, 12, 15, 20],
"500": [12, 20, 22, 25],
"403": [10, 20, 30]
    }
• Task: Use a Set Comprehension to create a new set containing only the Server IDs that
experienced every type of error (404, 500, AND 403).
• Task: Identify the "Critical Servers"—these are servers that experienced a "500" error but
never experienced a "404" error."""

logs = {
    "404": [10, 12, 15, 20],
    "500": [12, 20, 22, 25],
    "403": [10, 20, 30]
}

# Task 1: Set Comprehension for servers with ALL error types (404, 500, 403)
# Uses set intersection to find common IDs across all lists.
all_errors = set(logs["404"]) & set(logs["500"]) & set(logs["403"])
print("Servers with all errors:", all_errors)

# Task 2: Identify "Critical Servers" (500 error, but never 404)
# Uses set difference: 500s minus 404s.
critical_servers = set(logs["500"]) - set(logs["404"])
print("Critical Servers (500 but no 404):", critical_servers)
