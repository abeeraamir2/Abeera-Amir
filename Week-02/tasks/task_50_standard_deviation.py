import numpy as np

# Use speed dataset to calculate standard deviation and variance
speed = [86, 87, 88, 86, 87, 85, 86]

# Standard Deviation
std_val = np.std(speed)
print("Standard Deviation:", std_val)

# Variance
var_val = np.var(speed)
print("Variance:", var_val)
