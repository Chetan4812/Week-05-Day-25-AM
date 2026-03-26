import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)
df['Age'] = df['Age'].fillna(df['Age'].median())

# Filter rows where Fare is greater than average
avg_fare = df['Fare'].mean()
above_avg = df[df['Fare'] > avg_fare]

print(f"Average Fare : £{avg_fare:.2f}")
print(f"Rows above average fare: {len(above_avg)} / {len(df)}")
print(above_avg[['Name', 'Fare', 'Pclass', 'Survived']].head())

# Filter rows where Age is greater than average
avg_age = df['Age'].mean()
above_avg_age = df[df['Age'] > avg_age]

print(f"\nAverage Age : {avg_age:.2f}")
print(f"Rows above average age: {len(above_avg_age)} / {len(df)}")
print(above_avg_age[['Name', 'Age', 'Pclass']].head())
