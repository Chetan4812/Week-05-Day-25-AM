# Week-05-Day-25-AM

**Dataset used:** Titanic (891 rows) — loaded directly via URL
(`https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv`)

To use your own CSV replace the `url` line with:
```python
df = pd.read_csv('your_file.csv')
```

---

# Part A — Concept Application (40%)

### Basic Exploration
*   Display first 5 and last 5 rows
*   Show shape and column names <br>
[Solution](basic_exploration.py)

### Data Cleaning
*   Identify missing values and percentage missing per column
*   Fill Age with median, Embarked with mode; drop Cabin (77% missing) <br>
[Solution](data_cleaning.py)

### Descriptive Statistics
*   Use `describe()` to summarize the dataset
*   Manually interpret mean, std, min, max for Age, Fare, and Survived <br>
[Solution](descriptive_statistics.py)

### Categorical Analysis
*   Find unique values for Sex, Pclass, Embarked, Survived
*   Show frequency count using `value_counts()` <br>
[Solution](categorical_analysis.py)

---

## Part B — Stretch Problem (30%)

*   Filter dataset using multiple conditions (female survivors in 1st/2nd class; high-fare non-survivors)
*   Create new columns: `AgeGroup` and `FareCategory` using `pd.cut()`
*   Sort by Fare (descending) and Age (ascending)
*   Group by Pclass and Sex, compute mean Age, Fare, and Survival Rate <br>
[Solution](stretch_problem.py)

---

## Part C — Interview Ready (20%)

**Q1 — What is EDA? Why is it important?**

EDA (Exploratory Data Analysis) is the process of examining a dataset before modelling — using statistical summaries, visualisations, and Pandas operations — to understand its structure, detect anomalies, find patterns, and check assumptions.

### Why EDA is important:
*   **Reveals missing data:** Without spotting and handling nulls, models silently fail or produce biased results.
*   **Detects outliers:** Extreme values (like Fare = £512) can distort model training if left unchecked.
*   **Guides feature selection:** Correlation and groupby analyses reveal which features are actually predictive.
*   **Uncovers distributions:** Knowing if a feature is skewed or normally distributed informs preprocessing choices (e.g., log-transform for right-skewed data).
*   **Prevents garbage-in-garbage-out:** Understanding the data before modelling is the single biggest factor in model quality.

**Q2 (Coding) — Filter rows where column value > average** <br>
[Solution](filter_above_average.py)

**Q3 — What insights can we get from `describe()`?**

`describe()` prints 8 summary statistics for every numeric column:

*   **count** — number of non-null entries; if count < total rows, the column has missing values
*   **mean** — average value; the "center of mass" of the data
*   **std** — standard deviation; how spread out values are around the mean
*   **min / max** — smallest and largest values; useful for catching data entry errors or outliers
*   **25% / 50% / 75%** — quartiles; comparing mean vs 50% (median) reveals skewness:
    *   `mean > median` → right (positive) skew — e.g., Fare column
    *   `mean ≈ median` → roughly symmetric — e.g., Age column

### Practical insights from Titanic `describe()`:
*   `Fare` has a very high std relative to mean → large outliers, right-skewed distribution
*   `Survived` mean ≈ 0.38 → only 38% of passengers survived
*   `Age` count < 891 → missing values exist before cleaning
*   `Pclass` min=1, max=3 → confirms 3 classes with no data errors

---

## Part D — AI-Augmented Task (10%)

### 1. Prompt AI:
*"Explain EDA steps using Pandas with examples."*

### 2. Document prompt and output

[AI Output](AI_output.md) for the above prompt

### 3. Evaluate Correctness

*   **Step coverage:** The AI correctly identified all major EDA steps — load, inspect, missing values, statistics, categorical analysis, filtering, and groupby. No step was missed or misrepresented.
*   **Code accuracy:** All Pandas methods used (`fillna`, `isnull`, `describe`, `value_counts`, `groupby`, `pd.cut`) are correct and idiomatic.
*   **Missing value strategy:** The AI correctly chose median for Age (robust to outliers) and mode for Embarked (categorical). This matches best practice.
*   **Checklist table:** The summary table at the end is accurate and a useful quick reference.

> **One improvement made:**
> The AI's EDA steps were generic. In our solutions we applied each step specifically to the Titanic dataset with real output values and interpretations (e.g., "Fare std = 49.7 → high spread, right-skewed") — making the analysis more meaningful than just runnable code.

### Runnability

All AI-provided snippets run without modification. The only requirement is `pip install pandas`.
