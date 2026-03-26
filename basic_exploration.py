import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Display first 5 rows
print("First 5 rows:")
print(df.head())

# Display last 5 rows
print("\nLast 5 rows:")
print(df.tail())

# Shape
print(f"\nShape: {df.shape}")
print(f"  Rows    : {df.shape[0]}")
print(f"  Columns : {df.shape[1]}")

# Column names
print(f"\nColumn Names:")
for col in df.columns:
    print(f"  {col}")
