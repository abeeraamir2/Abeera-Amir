import numpy as np
from scipy import stats

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

# Mean
mean_val = np.mean(speed)
print("Mean:", mean_val)

# Median
median_val = np.median(speed)
print("Median:", median_val)

# Mode
mode_val = stats.mode(speed, keepdims=True)
print("Mode:", mode_val.mode[0])
