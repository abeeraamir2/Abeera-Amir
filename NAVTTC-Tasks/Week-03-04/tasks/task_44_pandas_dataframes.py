import pandas as pd

# Data for DataFrame
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

# Create DataFrame
df = pd.DataFrame(data)
print("DataFrame:\n", df)

# Locate row using loc
print("\nFirst row using loc[0]:\n", df.loc[0])
print("\nFirst two rows using loc[[0, 1]]:\n", df.loc[[0, 1]])

# DataFrame with named indexes
df_named = pd.DataFrame(data, index=["day1", "day2", "day3"])
print("\nDataFrame with named indexes:\n", df_named)
print("\nLocate day2:\n", df_named.loc["day2"])
