import numpy as np

# Generate random integer from 0 to 100
rand_int = np.random.randint(100)
print("Random integer:", rand_int)

# Generate random float between 0 and 1
rand_float = np.random.rand()
print("Random float:", rand_float)

# Generate 1-D array of random integers
arr_randint = np.random.randint(100, size=5)
print("1-D random integers:", arr_randint)

# Generate 2-D array of random floats (3 rows, 2 columns)
arr_rand2d = np.random.rand(3, 2)
print("\n2-D random floats:\n", arr_rand2d)

# Generate random value from a list using choice()
choice_val = np.random.choice([3, 5, 7, 9], size=(2, 3))
print("\nRandom choices from [3, 5, 7, 9]:\n", choice_val)

# Shuffling array in-place
arr = np.array([1, 2, 3, 4, 5])
np.random.shuffle(arr)
print("\nShuffled array:", arr)
