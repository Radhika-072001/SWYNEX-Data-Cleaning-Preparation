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
# Task 2 - Exploratory Data Analysis

## Overview

This task focuses on performing Exploratory Data Analysis (EDA) on the cleaned Titanic dataset obtained from Task 1.

The main objective is to understand the dataset, identify important patterns and trends, calculate statistical measures, and visualize useful insights using Python.

## Dataset

The dataset used for this task is the cleaned Titanic dataset created during Task 1.

**Dataset:** `cleaned_train.csv`

## Tools and Technologies

* Python
* Pandas
* Matplotlib
* Seaborn
* Jupyter Notebook / VS Code

## Objectives

The objectives of this task are:

* Explore the cleaned dataset.
* Calculate important statistical measures.
* Analyze passenger survival patterns.
* Identify relationships between different variables.
* Create meaningful data visualizations.
* Identify at least five useful insights from the dataset.

## Exploratory Data Analysis

The following analysis was performed:

### 1. Survival Count

A count plot was created to compare the number of passengers who survived and those who did not.

### 2. Survival by Gender

The survival rates of male and female passengers were analyzed to identify differences between the two groups.

### 3. Survival by Passenger Class

Passenger survival was compared across first, second, and third classes.

### 4. Age Distribution

A histogram with a KDE curve was used to understand the age distribution of passengers.

### 5. Fare Distribution

The distribution of passenger ticket fares was analyzed using a histogram.

### 6. Age vs Fare

A scatter plot was created to examine the relationship between passenger age and ticket fare, with survival status included for comparison.

## Statistical Analysis

The following statistical measures were calculated:

* Mean age
* Median age
* Average ticket fare
* Overall survival rate
* Survival rate by gender
* Survival rate by passenger class

## Key Insights

1. The overall survival rate was calculated to understand the proportion of passengers who survived the Titanic disaster.

2. Survival rates differed between male and female passengers, showing a clear relationship between gender and survival.

3. Passenger class had an important relationship with survival, with survival rates varying across first, second, and third class.

4. The age distribution shows that the Titanic dataset contains passengers from a wide range of age groups, including children and adults.

5. Ticket fares were highly varied, indicating differences in passenger class and travel conditions.

## Conclusion

Exploratory Data Analysis helped identify important patterns and relationships within the Titanic dataset. The visualizations and statistical analysis provide a better understanding of how factors such as gender, passenger class, age, and fare were associated with passenger survival.

This analysis demonstrates how Python-based EDA can be used to extract meaningful insights from a real-world dataset.
