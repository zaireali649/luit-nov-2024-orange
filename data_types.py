# Common Data Types in Python

# Integer (int) - Used for whole numbers
age = 25
print("Integer example (age):", age)

# Float (float) - Used for decimal numbers
temperature = 36.6
print("Float example (temperature):", temperature)

# String (str) - Used for text
name = "Alice"
print("String example (name):", name)

# Boolean (bool) - Used for True/False values
is_student = True
print("Boolean example (is_student):", is_student)

# List (list) - Ordered collection of items, can hold mixed data types
fruits = ["apple", "banana", "cherry"]
print("List example (fruits):", fruits)

# Dictionary (dict) - Collection of key-value pairs, useful for storing related data
person = {"name": "Alice", "age": 25, "is_student": True}
print("Dictionary example (person):", person)

# Set (set) - Unordered collection of unique items, useful for removing duplicates
unique_numbers = {1, 2, 3, 3, 4}
print("Set example (unique_numbers):", unique_numbers)

# None (NoneType) - Represents the absence of a value or a null value
address = None
print("NoneType example (address):", address)

# Practical usage examples

# Adding two integers
a = 5
b = 10
sum_result = a + b
print("Sum of two integers:", sum_result)

# Concatenating two strings
greeting = "Hello"
name = "Alice"
full_greeting = greeting + ", " + name + "!"
print("Concatenated string:", full_greeting)

# Accessing elements in a list
first_fruit = fruits[0]  # Accessing the first item in the list
print("First fruit in the list:", first_fruit)

# Updating values in a dictionary
person["age"] = 26  # Changing the age in the dictionary
print("Updated dictionary (person):", person)

# Adding an item to a set
unique_numbers.add(5)
print("Set after adding an item:", unique_numbers)

# Checking the type of each variable
print("Type of 'age':", type(age))
print("Type of 'temperature':", type(temperature))
print("Type of 'name':", type(name))
print("Type of 'is_student':", type(is_student))
print("Type of 'fruits':", type(fruits))
print("Type of 'person':", type(person))
print("Type of 'unique_numbers':", type(unique_numbers))
print("Type of 'address':", type(address))
