import numpy as np

# Shape of a 2-D array (rows, columns)
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("2-D array shape:", arr.shape)

# Shape of a 5-D array
arr_5d = np.array([1, 2, 3, 4], ndmin=5)
print("5-D array:", arr_5d)
print("Shape of 5-D array:", arr_5d.shape)
