### EDA Steps Using Pandas with Examples

Exploratory Data Analysis (EDA) is the process of examining a dataset to understand its structure, spot anomalies, discover patterns, and test initial hypotheses before building any model.

#### Step 1 — Load and Inspect

```python
import pandas as pd

df = pd.read_csv('titanic.csv')

print(df.head())          # first 5 rows
print(df.tail())          # last 5 rows
print(df.shape)           # (rows, columns)
print(df.columns.tolist()) # column names
print(df.dtypes)          # data types per column
print(df.info())          # non-null counts + dtypes
```

#### Step 2 — Missing Values

```python
print(df.isnull().sum())                          # count per column
print((df.isnull().sum() / len(df) * 100).round(2)) # as percentage

# Handle missing values
df['Age'] = df['Age'].fillna(df['Age'].median())  # fill with median
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])  # fill with mode
df.drop(columns=['Cabin'], inplace=True)          # drop high-null column
```

#### Step 3 — Descriptive Statistics

```python
print(df.describe())
# count  — non-null entries (reveals missing values)
# mean   — central tendency
# std    — spread / variability
# min/max — value range; useful for spotting outliers
# 25/50/75% — quartiles; compare mean vs median for skewness
```

#### Step 4 — Categorical Analysis

```python
print(df['Sex'].unique())          # unique values
print(df['Pclass'].nunique())      # number of unique values
print(df['Embarked'].value_counts()) # frequency count per category
```

#### Step 5 — Filtering and Grouping

```python
# Filter: multiple conditions
survivors = df[(df['Survived'] == 1) & (df['Sex'] == 'female')]

# New column from existing data
df['AgeGroup'] = pd.cut(df['Age'], bins=[0, 18, 35, 60, 100],
                         labels=['Minor', 'YoungAdult', 'Adult', 'Senior'])

# Sort
df_sorted = df.sort_values('Fare', ascending=False)

# Groupby + mean
print(df.groupby('Pclass')[['Fare', 'Survived']].mean())
```

> *Source: Pandas documentation — pandas.pydata.org*

### Key EDA Checklist

| Step | Pandas Method | Purpose |
| :--- | :--- | :--- |
| Load data | `pd.read_csv()` | Read dataset into DataFrame |
| Inspect | `head()`, `shape`, `dtypes` | Understand structure |
| Missing values | `isnull().sum()` | Find gaps in data |
| Statistics | `describe()` | Summarise numeric columns |
| Categorical | `value_counts()` | Frequency distribution |
| Filter | Boolean indexing | Extract meaningful subsets |
| Group | `groupby().mean()` | Aggregate by category |
