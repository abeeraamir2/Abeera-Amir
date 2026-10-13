import os
import pandas as pd

# Load CSV file
csv_path = os.path.join(os.path.dirname(__file__), "..", "data", "health_data.csv")
df = pd.read_csv(csv_path)

# Display CSV content
print("Reading CSV Data:")
print(df.to_string())

# Display max rows setting
print("\nMax rows display setting:", pd.options.display.max_rows)
