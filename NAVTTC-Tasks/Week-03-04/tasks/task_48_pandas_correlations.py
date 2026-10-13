import os
import pandas as pd

# Load CSV file
csv_path = os.path.join(os.path.dirname(__file__), "..", "data", "health_data.csv")
df = pd.read_csv(csv_path)

# Calculate correlation matrix
corr_matrix = df.corr()

print("Correlation Matrix:")
print(corr_matrix)
