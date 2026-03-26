import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Identify missing values
print("Missing values per column:")
print(df.isnull().sum())
print(f"\nTotal missing: {df.isnull().sum().sum()}")

# Percentage missing
missing_pct = (df.isnull().sum() / len(df) * 100).round(2)
print("\nMissing percentage:")
print(missing_pct[missing_pct > 0])

# Fill Age with median (robust to outliers)
df['Age'] = df['Age'].fillna(df['Age'].median())

# Fill Embarked with mode (most frequent port)
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Drop Cabin — 77% missing, not recoverable
df.drop(columns=['Cabin'], inplace=True)

print("\nMissing values after cleaning:")
print(df.isnull().sum())
print(f"\nCleaned dataset shape: {df.shape}")
