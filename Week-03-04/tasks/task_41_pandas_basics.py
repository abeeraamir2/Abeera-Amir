import pandas as pd

# Basic dataset
dataset = {
    "cars": ["BMW", "Volvo", "Ford"],
    "passings": [3, 7, 2]
}

# Create DataFrame
df = pd.DataFrame(dataset)
print("Pandas DataFrame:")
print(df)
