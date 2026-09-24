# Task 1: Data Cleaning & Preparation

## Objective

The objective of this task is to clean and prepare a public dataset for further analysis and machine learning.

## Dataset

The Titanic dataset was used for this task.

The dataset contains information about passengers, including:

* Passenger ID
* Survival status
* Passenger class
* Name
* Sex
* Age
* Number of siblings/spouses
* Number of parents/children
* Ticket
* Fare
* Cabin
* Port of Embarkation

## Data Cleaning Steps

The following data cleaning and preparation steps were performed:

1. Loaded the Titanic dataset using Pandas.
2. Inspected the first few records.
3. Checked the dataset shape and column names.
4. Checked for missing values.
5. Filled missing `Age` values using the median.
6. Filled missing `Embarked` values using the mode.
7. Removed the `Cabin` column because it contained a large number of missing values.
8. Checked for duplicate records.
9. Removed duplicate records.
10. Checked and converted numerical columns to appropriate data types.
11. Checked categorical columns for inconsistent values.
12. Standardized the `Sex` and `Embarked` columns.
13. Performed a final check for missing values and data
