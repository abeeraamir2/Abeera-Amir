import numpy as np

# Splitting 1-D array into 3 parts
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print("Split 1-D array into 3:")
for part in newarr:
    print(part)

# Accessing individual split parts
print("\nFirst part:", newarr[0])
print("Second part:", newarr[1])
print("Third part:", newarr[2])

# Splitting 2-D array
arr_2d = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr_2d = np.array_split(arr_2d, 3)
print("\nSplit 2-D array:")
for part in newarr_2d:
    print(part)

# Horizontal split using hsplit
h_split = np.hsplit(np.array([[1, 2, 3, 4], [5, 6, 7, 8]]), 2)
print("\nHorizontal split:\n", h_split)
