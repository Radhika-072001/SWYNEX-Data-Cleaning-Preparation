import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("data/cleaned_train.csv")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Dataset shape
print("\nDataset Shape:")
print(df.shape)

# Column information
print("\nDataset Information:")
print(df.info())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Statistical summary
print("\nStatistical Summary:")
print(df.describe())
# ==========================================
# TASK 2 - EXPLORATORY DATA ANALYSIS
# ==========================================

# 1. Survival Count
plt.figure(figsize=(7, 5))
sns.countplot(data=df, x="Survived")
plt.title("Survival Count")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Number of Passengers")
plt.show()


# 2. Survival by Gender
plt.figure(figsize=(7, 5))
sns.countplot(data=df, x="Sex", hue="Survived")
plt.title("Survival by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Passengers")
plt.legend(title="Survived", labels=["No", "Yes"])
plt.show()


# 3. Survival by Passenger Class
plt.figure(figsize=(7, 5))
sns.countplot(data=df, x="Pclass", hue="Survived")
plt.title("Survival by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Number of Passengers")
plt.legend(title="Survived", labels=["No", "Yes"])
plt.show()


# 4. Age Distribution
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="Age", bins=30, kde=True)
plt.title("Age Distribution of Passengers")
plt.xlabel("Age")
plt.ylabel("Number of Passengers")
plt.show()


# 5. Fare Distribution
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="Fare", bins=30, kde=True)
plt.title("Fare Distribution")
plt.xlabel("Fare")
plt.ylabel("Number of Passengers")
plt.show()


# 6. Age vs Fare
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="Age", y="Fare", hue="Survived")
plt.title("Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()


# ==========================================
# IMPORTANT STATISTICS
# ==========================================

print("\n========== IMPORTANT STATISTICS ==========")

print("\nAverage Age:")
print(df["Age"].mean())

print("\nMedian Age:")
print(df["Age"].median())

print("\nAverage Fare:")
print(df["Fare"].mean())

print("\nSurvival Rate:")
print(df["Survived"].mean() * 100)

print("\nSurvival Rate by Gender:")
print(df.groupby("Sex")["Survived"].mean() * 100)

print("\nSurvival Rate by Passenger Class:")
print(df.groupby("Pclass")["Survived"].mean() * 100)
# ==========================================
# 5 USEFUL INSIGHTS
# ==========================================

print("\n========== 5 USEFUL INSIGHTS ==========")

# Insight 1 - Overall Survival
survival_rate = df["Survived"].mean() * 100
print(f"1. Overall, {survival_rate:.2f}% of passengers survived.")


# Insight 2 - Gender
gender_survival = df.groupby("Sex")["Survived"].mean() * 100
print("\n2. Survival Rate by Gender:")
print(gender_survival)


# Insight 3 - Passenger Class
class_survival = df.groupby("Pclass")["Survived"].mean() * 100
print("\n3. Survival Rate by Passenger Class:")
print(class_survival)


# Insight 4 - Average Age
average_age = df["Age"].mean()
print(f"\n4. The average age of passengers was {average_age:.2f} years.")


# Insight 5 - Average Fare
average_fare = df["Fare"].mean()
print(f"5. The average ticket fare was {average_fare:.2f}.")