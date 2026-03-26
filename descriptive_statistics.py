import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)
df['Age'] = df['Age'].fillna(df['Age'].median())

# Full describe()
print("describe() output:")
print(df.describe())

print("\n── Manual Interpretation ────────────────────────────────────")

# Age
print(f"\nAge:")
print(f"  Mean : {df['Age'].mean():.2f}  → average passenger was ~{df['Age'].mean():.0f} years old")
print(f"  Std  : {df['Age'].std():.2f}  → ages vary ~{df['Age'].std():.0f} years from the mean")
print(f"  Min  : {df['Age'].min():.2f}   → youngest passenger on board")
print(f"  Max  : {df['Age'].max():.2f}  → oldest passenger on board")

# Fare
print(f"\nFare:")
print(f"  Mean : {df['Fare'].mean():.2f}  → average ticket cost £{df['Fare'].mean():.2f}")
print(f"  Std  : {df['Fare'].std():.2f}  → very high spread; wide price range across classes")
print(f"  Min  : {df['Fare'].min():.2f}   → some passengers paid nothing")
print(f"  Max  : {df['Fare'].max():.2f} → most expensive ticket; likely 1st class luxury suite")

# Survived
print(f"\nSurvived:")
print(f"  Mean : {df['Survived'].mean():.4f} → ~{df['Survived'].mean()*100:.1f}% survival rate overall")
