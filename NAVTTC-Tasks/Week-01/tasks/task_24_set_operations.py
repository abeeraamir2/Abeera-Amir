# Creating sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print("Set A:", set_a)
print("Set B:", set_b)

# Adding elements
set_a.add(10)
print("Set A after add(10):", set_a)

# Removing elements
set_a.discard(10)
print("Set A after discard(10):", set_a)

# Set operations
print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference (A - B):", set_a - set_b)
print("Symmetric Difference:", set_a ^ set_b)
