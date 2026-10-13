import numpy as np

# Searching array using where()
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print("Indexes where value is 4:", x[0])

# Find indexes where elements are even
even_idx = np.where(arr % 2 == 0)
print("Indexes of even numbers:", even_idx[0])

# Find indexes where elements are odd
odd_idx = np.where(arr % 2 != 0)
print("Indexes of odd numbers:", odd_idx[0])

# searchsorted() on sorted array (finds insertion index)
sorted_arr = np.array([6, 7, 8, 9])
pos = np.searchsorted(sorted_arr, 7)
print("\nPosition to insert 7:", pos)

# Multiple values with searchsorted
positions = np.searchsorted(sorted_arr, [2, 4, 6])
print("Positions to insert [2, 4, 6]:", positions)
