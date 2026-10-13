import pandas as pd

# Creating a simple Pandas Series from list
a = [1, 7, 2]
my_series = pd.Series(a)
print("Series with default index:\n", my_series)
print("\nFirst value:", my_series[0])

# Creating Series with custom labels
my_labeled = pd.Series(a, index=["x", "y", "z"])
print("\nSeries with custom labels:\n", my_labeled)
print("Value with label 'y':", my_labeled["y"])

# Creating Series from a dictionary (Key/Value object)
calories = {"day1": 420, "day2": 380, "day3": 390}
cal_series = pd.Series(calories)
print("\nSeries from dictionary:\n", cal_series)
