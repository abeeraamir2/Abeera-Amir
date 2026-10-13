import os
import pandas as pd

# Load CSV file
csv_path = os.path.join(os.path.dirname(__file__), "..", "data", "health_data.csv")
df = pd.read_csv(csv_path)

# Viewing the first 5 rows
print("First 5 rows (head):")
print(df.head())

# Viewing the last 5 rows
print("\nLast 5 rows (tail):")
print(df.tail())

# Information about the data
print("\nData info:")
df.info()
