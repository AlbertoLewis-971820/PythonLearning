#Learning Lists and Tuples in Python

# LISTS
# A list is an ordered, mutable collection of elements enclosed in square brackets.
# Lists can contain elements of any data type (integers, strings, floats, etc.) and can store duplicates.
# Elements are accessed by their index position (starting from 0). Lists are mutable, meaning you can add,
# remove, or modify elements after creation. Lists are ideal for storing sequences of items that may change.
# Common operations include append() to add elements, remove() to delete specific values, and indexing to access items.

fruits = ['apple', 'banana', 'cherry']

print("Fruits List:", fruits)


# Accessing elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])


# Adding elements
fruits.append('date')
print("After appending date:", fruits)

# Removing elements
fruits.remove('banana')
print("After removing banana:", fruits)

# TUPLES
# A tuple is an ordered, immutable collection of elements enclosed in parentheses.
# Tuples can contain elements of any data type and can store duplicates, similar to lists.
# Elements are accessed by their index position (starting from 0), just like lists.
# Tuples are immutable, meaning once created, you cannot add, remove, or modify elements.
# Tuples are useful when you need a collection of data that should not be changed, providing data protection
# and slightly better performance than lists. Tuples can be used as dictionary keys, whereas lists cannot.

coordinates = (10.0, 20.0)
print("Coordinates Tuple:", coordinates)

# Accessing elements
print("X coordinate:", coordinates[0])
print("Y coordinate:", coordinates[1])

# Tuples are immutable, so we cannot add or remove elements
# The following line would raise an error if uncommented
# coordinates[0] = 15.0
print("Tuples are immutable; cannot modify elements.")


