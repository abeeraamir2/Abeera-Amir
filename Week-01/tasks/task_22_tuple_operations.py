# Creating a tuple
my_tuple = ("apple", "banana", "cherry", "apple")
print("Tuple:", my_tuple)

# Accessing elements
print("First item:", my_tuple[0])
print("Last item:", my_tuple[-1])
print("Slice [1:3]:", my_tuple[1:3])

# Tuple methods
print("Count of 'apple':", my_tuple.count("apple"))
print("Index of 'banana':", my_tuple.index("banana"))

# Tuple unpacking
a, b, c, d = my_tuple
print("Unpacked values:", a, b, c, d)
