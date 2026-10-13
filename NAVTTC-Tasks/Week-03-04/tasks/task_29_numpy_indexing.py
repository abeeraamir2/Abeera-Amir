import numpy as np

# 1-D Array Indexing
arr_1d = np.array([10, 20, 30, 40])
print("First element:", arr_1d[0])
print("Second element:", arr_1d[1])
print("Sum of 3rd and 4th:", arr_1d[2] + arr_1d[3])

# 2-D Array Indexing (row, column)
arr_2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("\nElement at 1st row, 2nd column:", arr_2d[0, 1])
print("Element at 2nd row, 5th column:", arr_2d[1, 4])

# 3-D Array Indexing
arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("\nElement at [0, 1, 2]:", arr_3d[0, 1, 2])

# Negative Indexing
print("\nLast element of 2nd dim:", arr_2d[1, -1])
