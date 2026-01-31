# Dictionaries
# A dictionary is an unordered, mutable collection of key-value pairs.
# Keys must be unique and immutable (strings, numbers, tuples), while values can be any data type.
# Dictionaries are ideal for storing related data that needs to be accessed by a specific identifier.
# Access values using keys, not by index position. Dictionaries provide fast lookups and are useful
# for mapping relationships between data. You can add, remove, or modify key-value pairs easily.

student = {'name': 'Alice', 'age': 20, 'grade': 'A'}
print("\nStudent Dictionary:", student)

# Accessing values using keys
print("Student name:", student['name'])
print("Student age:", student['age'])

# Adding a new key-value pair
student['gpa'] = 3.8
print("After adding GPA:", student)

# Modifying an existing value
student['age'] = 21
print("After updating age:", student)

# Removing a key-value pair
del student['grade']
print("After removing grade:", student)


# Sets
# A set is an unordered, mutable collection of unique elements.
# Sets do not allow duplicate values; any duplicates are automatically removed.
# Elements in a set must be immutable (strings, numbers, tuples) but the set itself can be modified.
# Sets are useful for membership testing, removing duplicates, and performing mathematical operations
# like union, intersection, and difference. Sets are faster than lists for checking if an element exists.

colors = {'red', 'blue', 'green'}
print("\nColors Set:", colors)

# Adding elements
colors.add('yellow')
print("After adding yellow:", colors)

# Attempting to add a duplicate (will be ignored)
colors.add('red')
print("After attempting to add red again:", colors)

# Removing elements
colors.remove('blue')
print("After removing blue:", colors)

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("\nSet1:", set1)
print("Set2:", set2)
print("Union (all elements):", set1 | set2)
print("Intersection (common elements):", set1 & set2)
print("Difference (in set1 but not set2):", set1 - set2)