import pandas as pd

# Check Pandas version
print("Pandas version:", pd.__version__)

# Create and display a simple DataFrame
dataset = {
    "cars": ["BMW", "Volvo", "Ford"],
    "passings": [3, 7, 2]
}
myvar = pd.DataFrame(dataset)
print("\nDataFrame:\n", myvar)
