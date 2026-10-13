import numpy as np

# 0-D array
a = np.array(42)
print("0-D array:", a)
print("Dimensions:", a.ndim)

# 1-D array
b = np.array([1, 2, 3, 4, 5])
print("\n1-D array:", b)
print("Dimensions:", b.ndim)

# 2-D array
c = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2-D array:\n", c)
print("Dimensions:", c.ndim)

# 3-D array
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print("\n3-D array:\n", d)
print("Dimensions:", d.ndim)

# Creating higher dimensional array using ndmin
arr = np.array([1, 2, 3, 4], ndmin=5)
print("\n5-D array:", arr)
print("Number of dimensions:", arr.ndim)
