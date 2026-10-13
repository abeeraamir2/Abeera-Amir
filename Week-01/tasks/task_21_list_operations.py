# Creating a list
fruits = ["apple", "banana", "cherry", "orange"]
print("Original list:", fruits)

# Accessing elements
print("First item:", fruits[0])
print("Last item:", fruits[-1])
print("Slice [1:3]:", fruits[1:3])

# Adding elements
fruits.append("mango")
print("After append:", fruits)

fruits.insert(1, "blueberry")
print("After insert:", fruits)

# Removing elements
fruits.remove("banana")
print("After remove:", fruits)

popped = fruits.pop()
print("Popped item:", popped)
print("After pop:", fruits)

# Sorting
fruits.sort()
print("Sorted list:", fruits)
