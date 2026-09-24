import pandas as pd

# =========================================================
# TASK 1: DATA CLEANING & PREPARATION
# =========================================================

# 1. Load Dataset
df = pd.read_csv("data/Titanic_train.csv")

print("========== ORIGINAL DATASET ==========")

# Display first 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Dataset shape
print("\nDataset Shape:")
print(df.shape)

# Column names
print("\nColumn Names:")
print(df.columns.tolist())


# =========================================================
# 2. Dataset Information
# =========================================================

print("\n========== DATASET INFORMATION ==========")
df.info()


# =========================================================
# 3. Statistical Summary
# =========================================================

print("\n========== STATISTICAL SUMMARY ==========")
print(df.describe())


# =========================================================
# 4. CHECK MISSING VALUES
# =========================================================

print("\n========== MISSING VALUES BEFORE CLEANING ==========")
print(df.isnull().sum())


# =========================================================
# 5. HANDLE MISSING VALUES
# =========================================================

# Fill missing Age values with median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill missing Embarked values with mode
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Drop Cabin because it contains many missing values
df.drop("Cabin", axis=1, inplace=True)


# =========================================================
# 6. CHECK MISSING VALUES AFTER CLEANING
# =========================================================

print("\n========== MISSING VALUES AFTER CLEANING ==========")
print(df.isnull().sum())


# =========================================================
# 7. CHECK DUPLICATE RECORDS
# =========================================================

print("\n========== DUPLICATE RECORDS ==========")

print("Duplicates Before Cleaning:")
print(df.duplicated().sum())

# Remove duplicate records
df.drop_duplicates(inplace=True)

print("Duplicates After Cleaning:")
print(df.duplicated().sum())


# =========================================================
# 8. CHECK DATA TYPES
# =========================================================

print("\n========== DATA TYPES ==========")
print(df.dtypes)


# =========================================================
# 9. CONVERT DATA TYPES IF REQUIRED
# =========================================================

# Convert PassengerId, Survived, Pclass and other numerical
# columns to numeric data types

df["PassengerId"] = pd.to_numeric(df["PassengerId"], errors="coerce")
df["Survived"] = pd.to_numeric(df["Survived"], errors="coerce")
df["Pclass"] = pd.to_numeric(df["Pclass"], errors="coerce")
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["SibSp"] = pd.to_numeric(df["SibSp"], errors="coerce")
df["Parch"] = pd.to_numeric(df["Parch"], errors="coerce")
df["Fare"] = pd.to_numeric(df["Fare"], errors="coerce")


# =========================================================
# 10. CHECK INCONSISTENT VALUES
# =========================================================

print("\n========== UNIQUE VALUES ==========")

print("\nSex:")
print(df["Sex"].unique())

print("\nEmbarked:")
print(df["Embarked"].unique())

print("\nSurvived:")
print(df["Survived"].unique())

print("\nPclass:")
print(df["Pclass"].unique())


# =========================================================
# 11. STANDARDIZE TEXT VALUES
# =========================================================

# Remove extra spaces and make text consistent

df["Sex"] = df["Sex"].str.strip().str.lower()
df["Embarked"] = df["Embarked"].str.strip().str.upper()


# =========================================================
# 12. FINAL CHECK FOR MISSING VALUES
# =========================================================

print("\n========== FINAL MISSING VALUE CHECK ==========")
print(df.isnull().sum())


# =========================================================
# 13. FINAL DATASET INFORMATION
# =========================================================

print("\n========== FINAL DATASET INFORMATION ==========")
print("Final Shape:", df.shape)

print("\nFinal Data Types:")
print(df.dtypes)

print("\nFinal First 5 Rows:")
print(df.head())


# =========================================================
# 14. SAVE CLEANED DATASET
# =========================================================

df.to_csv("data/cleaned_train.csv", index=False)

print("\n========================================")
print("DATA CLEANING COMPLETED SUCCESSFULLY!")
print("Cleaned dataset saved as:")
print("data/cleaned_train.csv")
print("========================================")