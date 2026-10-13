# Iterating over range
for i in range(5):
    print("Index:", i)

# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)

# Multiplication table for 3
for i in range(1, 6):
    print("3 x", i, "=", 3 * i)

# For-else example
numbers = [1, 2, 3, 4]
for num in numbers:
    if num == 5:
        print("Found 5")
        break
else:
    print("5 not found in list")
