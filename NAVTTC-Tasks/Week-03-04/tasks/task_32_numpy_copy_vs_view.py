import numpy as np

# Copy example
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print("Original array after change:", arr)
print("Copy array (not changed):   ", x)

# View example
arr2 = np.array([1, 2, 3, 4, 5])
y = arr2.view()
arr2[0] = 99

print("\nOriginal array after change:", arr2)
print("View array (also changed):  ", y)

# Check if array owns its data with .base
print("\nCopy base attribute (owns data):", x.base)
print("View base attribute (shares data):", y.base)
