import numpy as np

# Joining 1-D arrays with concatenate
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
joined_1d = np.concatenate((arr1, arr2))
print("Joined 1-D array:", joined_1d)

# Joining 2-D arrays along rows (axis=0) and columns (axis=1)
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

concat_axis0 = np.concatenate((a, b), axis=0)
print("\nConcatenate axis 0 (rows):\n", concat_axis0)

concat_axis1 = np.concatenate((a, b), axis=1)
print("\nConcatenate axis 1 (columns):\n", concat_axis1)

# Joining arrays using stack, hstack, vstack
stacked = np.stack((arr1, arr2), axis=1)
print("\nStack along axis 1:\n", stacked)

h_stacked = np.hstack((arr1, arr2))
print("Horizontal stack (hstack):", h_stacked)

v_stacked = np.vstack((arr1, arr2))
print("Vertical stack (vstack):\n", v_stacked)
