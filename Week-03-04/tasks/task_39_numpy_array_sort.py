import numpy as np

# Sorting numerical array
arr = np.array([3, 2, 0, 1])
print("Sorted numbers:", np.sort(arr))

# Sorting alphabetically
fruits = np.array(["banana", "cherry", "apple"])
print("Sorted strings:", np.sort(fruits))

# Sorting boolean array
bool_arr = np.array([True, False, True])
print("Sorted booleans:", np.sort(bool_arr))

# Sorting 2-D array 
arr_2d = np.array([[3, 2, 4], [5, 0, 1]])
print("\nSorted 2-D array:\n", np.sort(arr_2d))
