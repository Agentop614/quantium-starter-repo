import pandas as pd
import glob
import os

# Find all CSV files in the data folder
files = glob.glob("data/daily_sales_data_*.csv")

# Read and combine all three files
df = pd.concat([pd.read_csv(file) for file in files], ignore_index=True)

# Keep only Pink Morsel
df = df[df["product"] == "pink morsel"]

# Convert price from "$3.00" to 3.00
df["price"] = df["price"].str.replace("$", "", regex=False).astype(float)

# Calculate total sales
df["sales"] = df["price"] * df["quantity"]

# Keep only required fields
output = df[["sales", "date", "region"]]

# Save the final output
output.to_csv("daily_sales.csv", index=False)

print("Data processing complete!")
print(f"Rows processed: {len(output)}")
print(output.head())