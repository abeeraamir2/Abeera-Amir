import numpy as np

# 1-D Array Slicing [start:end:step]
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print("Elements from index 1 to 5:", arr[1:5])
print("Elements from index 4 to end:", arr[4:])
print("Elements from beginning to index 4:", arr[:4])
print("Negative slicing (-3 to -1):", arr[-3:-1])
print("Step slicing (every other element):", arr[1:5:2])
print("Return every other element in whole array:", arr[::2])

# 2-D Array Slicing
arr_2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("\nFrom 2nd row, slice elements 1 to 4:", arr_2d[1, 1:4])
print("From both rows, return index 2:", arr_2d[0:2, 2])
print("From both rows, slice index 1 to 4:\n", arr_2d[0:2, 1:4])
