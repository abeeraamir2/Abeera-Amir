import numpy as np

# Checking data type of an array
arr1 = np.array([1, 2, 3, 4])
print("Integer array dtype:", arr1.dtype)

arr2 = np.array(["apple", "banana", "cherry"])
print("String array dtype:", arr2.dtype)

# Creating arrays with a defined data type
arr3 = np.array([1, 2, 3, 4], dtype="S")
print("\nString array:", arr3)
print("Data type:", arr3.dtype)

arr4 = np.array([1, 2, 3, 4], dtype="i4")
print("4-byte integer dtype:", arr4.dtype)

# Converting data types using astype()
float_arr = np.array([1.1, 2.1, 3.1])
int_arr = float_arr.astype("i")
print("\nConverted to integer:", int_arr)
print("New dtype:", int_arr.dtype)

# Converting integer to boolean
bool_arr = np.array([1, 0, 3]).astype(bool)
print("Converted to boolean:", bool_arr)
