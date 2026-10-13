import numpy as np

# Reshape from 1-D to 2-D (4 rows, 3 columns)
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr_2d = arr.reshape(4, 3)
print("Reshaped to 2-D:\n", newarr_2d)

# Reshape from 1-D to 3-D (2 arrays, each 3x2)
newarr_3d = arr.reshape(2, 3, 2)
print("\nReshaped to 3-D:\n", newarr_3d)

# Unknown dimension using -1 (NumPy calculates remaining dimension)
unknown_arr = arr.reshape(2, 2, -1)
print("\nReshaped with -1:\n", unknown_arr)

# Flattening the array back to 1-D
flattened = newarr_2d.reshape(-1)
print("\nFlattened array:", flattened)
