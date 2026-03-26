import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Unique values for each categorical column
cat_cols = ['Sex', 'Pclass', 'Embarked', 'Survived']

print("Unique values:")
for col in cat_cols:
    print(f"  {col}: {df[col].unique()}")

# Frequency counts
print("\nFrequency Counts:")

print("\nSex:")
print(df['Sex'].value_counts())

print("\nPassenger Class (Pclass):")
print(df['Pclass'].value_counts().sort_index())

print("\nEmbarked (Port of Embarkation):")
print(df['Embarked'].value_counts())
# C = Cherbourg, Q = Queenstown, S = Southampton

print("\nSurvived:")
print(df['Survived'].value_counts())
surv_rate = df['Survived'].mean() * 100
print(f"  Survival rate: {surv_rate:.1f}%")
