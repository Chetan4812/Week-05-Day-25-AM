import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)
df['Age']      = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
df.drop(columns=['Cabin'], inplace=True)

# ── 1. Filter with multiple conditions ───────────────────────────────────────

# Female survivors in 1st or 2nd class
filtered = df[(df['Sex'] == 'female') & (df['Survived'] == 1) & (df['Pclass'] <= 2)]
print("Filter — Female survivors in 1st/2nd class:")
print(filtered[['Name', 'Sex', 'Pclass', 'Age', 'Fare']].head())
print(f"  Count: {len(filtered)}\n")

# High-fare passengers who did not survive
high_fare_lost = df[(df['Fare'] > df['Fare'].quantile(0.75)) & (df['Survived'] == 0)]
print("Filter — High-fare passengers who did not survive:")
print(high_fare_lost[['Name', 'Fare', 'Pclass', 'Survived']].head())
print(f"  Count: {len(high_fare_lost)}\n")

# ── 2. Create a new column based on existing data ────────────────────────────

# AgeGroup: bucket passengers into age categories
df['AgeGroup'] = pd.cut(df['Age'],
                         bins=[0, 12, 18, 35, 60, 100],
                         labels=['Child', 'Teen', 'YoungAdult', 'Adult', 'Senior'])

print("New column 'AgeGroup' — value counts:")
print(df['AgeGroup'].value_counts().sort_index())
print()

# FareCategory: label fare level
df['FareCategory'] = pd.cut(df['Fare'],
                              bins=[0, 15, 50, 100, 600],
                              labels=['Low', 'Medium', 'High', 'VeryHigh'])
print("New column 'FareCategory' — value counts:")
print(df['FareCategory'].value_counts().sort_index())
print()

# ── 3. Sort by a numerical column ────────────────────────────────────────────

# Sort by Fare descending — most expensive tickets first
df_sorted_fare = df.sort_values('Fare', ascending=False)
print("Top 5 passengers by Fare:")
print(df_sorted_fare[['Name', 'Fare', 'Pclass', 'Survived']].head())
print()

# Sort by Age ascending — youngest first
df_sorted_age = df.sort_values('Age', ascending=True)
print("5 youngest passengers:")
print(df_sorted_age[['Name', 'Age', 'Pclass', 'Survived']].head())
print()

# ── 4. Group and compute mean ─────────────────────────────────────────────────

# Group by Pclass → mean of Age, Fare, Survived
grouped = df.groupby('Pclass')[['Age', 'Fare', 'Survived']].mean().round(2)
grouped.columns = ['Mean Age', 'Mean Fare', 'Survival Rate']
grouped['Survival Rate'] = (grouped['Survival Rate'] * 100).round(1)
print("Grouped by Pclass — Mean values:")
print(grouped)
print()

# Group by Sex → mean survival
print("Grouped by Sex — Mean Survived:")
print(df.groupby('Sex')['Survived'].mean().round(3))
