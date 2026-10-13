import os
import pandas as pd

csv_path = os.path.join(os.path.dirname(__file__), "..", "data", "health_data.csv")
df = pd.read_csv(csv_path)

print("Original Data Info:")
print(df.isnull().sum())

# 1. Removing empty rows with dropna()
df_dropped = df.dropna()
print("\nRows after dropna():", len(df_dropped))

# 2. Filling empty values with Mean
df_filled = df.copy()
mean_calories = df["Calories"].mean()
df_filled["Calories"].fillna(mean_calories, inplace=True)
print(f"\nMissing calories filled with mean ({mean_calories:.2f}):")
print(df_filled.isnull().sum())

# 3. Removing duplicates
print("\nNumber of rows before removing duplicates:", len(df_filled))
df_cleaned = df_filled.drop_duplicates()
print("Number of rows after removing duplicates:", len(df_cleaned))
