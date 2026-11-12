# Titanic Passenger Data Explorer CLI

A Python-based command-line application for exploring, inspecting, and profiling the Titanic passenger dataset. The project focuses on Python fundamentals, CSV processing, data validation, and data-quality analysis using Python's built-in libraries.

## Overview

The Titanic Passenger Data Explorer CLI reads a CSV dataset and generates useful insights about its structure, contents, and data quality.

It performs schema validation, identifies missing values, analyzes categorical distributions, detects duplicate records, and validates numeric and categorical data against predefined rules.

The project was developed as part of my Python fundamentals and AI/ML preparation journey, with an emphasis on practical implementation rather than tutorial-based learning.

## Features

### 1. CSV Loading and Dataset Inspection
- Load CSV files using Python's `csv` module.
- Validate file existence and file paths.
- Inspect column names and total records.
- Display the first five records.
- Validate required columns.
- Detect malformed rows, including missing or extra fields.

### 2. Missing Value Analysis
- Identify missing values in each column.
- Support configurable missing-value markers.
- Calculate missing-value counts and percentages.
- Generate a column-wise missing-value report.

### 3. Categorical Frequency Analysis
- Calculate the frequency distribution of categorical columns.
- Analyze passenger attributes such as `Sex`, `Pclass`, and `Embarked`.
- Use Python's `collections.Counter`.

### 4. Unique Value Analysis
- Identify distinct values in selected columns.
- Remove duplicate values using Python sets.
- Return sorted unique values.

### 5. Duplicate Detection
- Identify exact duplicate records across all columns.
- Detect duplicate `PassengerId` values independently.
- Report duplicate occurrence counts.

### 6. Numeric Data Validation
- Validate numeric data types using `int` and `float`.
- Detect values that cannot be converted into numeric types.
- Enforce minimum-value constraints.
- Detect non-finite numeric values such as `NaN` and infinity.
- Handle missing values separately from invalid values.

### 7. Categorical Data Validation
- Validate categorical values against predefined allowed categories.
- Detect unexpected or inconsistent values.
- Normalize leading and trailing whitespace before validation.

### 8. Required Field Validation
- Define mandatory fields.
- Identify records with missing values in required columns.
- Report field-level validation errors.

## Tech Stack

| Technology | Usage |
|---|---|
| Python 3 | Core programming language |
| `csv` | CSV file processing |
| `pathlib` | File and directory handling |
| `collections.Counter` | Frequency and duplicate analysis |
| `math.isfinite` | Numeric validation |
| Python sets and dictionaries | Data processing and validation |

**External dependencies:** None. The current implementation uses Python's standard library.

## Project Structure

```text
Titanic-Passenger-Data-Explorer-CLI/
│
├── data/
│   └── raw/
│       └── train.csv
│
├── main.py
├── .gitignore
└── README.md
```

## Dataset

This project uses the Titanic training dataset containing passenger information and survival outcomes.

The dataset includes 891 passenger records and 12 columns, including:

- PassengerId
- Survived
- Pclass
- Name
- Sex
- Age
- SibSp
- Parch
- Ticket
- Fare
- Cabin
- Embarked

Place the dataset at:

```text
data/raw/train.csv
```

The application expects the CSV file to contain the required columns used by the analysis.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/astik77/Titanic-Passenger-Data-Explorer-CLI.git

cd Titanic-Passenger-Data-Explorer-CLI
```

### 2. Create a virtual environment

Windows:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Add the dataset

Ensure that `train.csv` is present inside:

```text
data/raw/
```

### 4. Run the application

```bash
python main.py
```

## Sample Output

The application generates multiple reports covering dataset information, missing values, categorical frequencies, unique values, duplicate detection, and validation results.

Example:

```text
=================================
     TITANIC DATA EXPLORER
=================================

[1] Dataset Information
Dataset: train.csv
Columns: 12
Total Records: 891

========================================
          MISSING VALUE REPORT
========================================

Column               Missing      Percentage
--------------------------------------------------
PassengerId          0            0.0%
Survived             0            0.0%
Pclass               0            0.0%
Name                 0            0.0%
Sex                  0            0.0%
Age                  177          19.87%
SibSp                0            0.0%
Parch                0            0.0%
Ticket               0            0.0%
Fare                 0            0.0%
Cabin                687          77.1%
Embarked             2            0.22%
```

## Python Concepts Practised

This project provided practical experience with:

- Variables, data types, loops, and conditional statements.
- Lists, tuples, dictionaries, and sets.
- Functions, parameters, and return values.
- File handling and CSV processing.
- Exception handling.
- Modules and standard-library imports.
- List and dictionary comprehensions.
- Iteration using `enumerate()`.
- Data validation and error handling.
- Reusable helper functions and separation of concerns.
- Virtual environments and Git version control.

## Future Improvements

Potential extensions to the project include:

- Refactoring the application into separate Python modules.
- Adding automated unit tests using `unittest` or `pytest`.
- Supporting JSON serialization and deserialization.
- Exporting data-quality reports to JSON and CSV.
- Adding summary statistics and numerical analysis using NumPy.
- Extending exploratory data analysis using Pandas and Matplotlib.

## Learning Objective

The primary objective of this project was to strengthen Python programming fundamentals through a practical data-processing application and establish a foundation for subsequent learning in NumPy, Pandas, data analysis, and machine learning.

---

**Project:** Titanic Passenger Data Explorer CLI  
**Language:** Python  
**Category:** Data Processing | Data Quality | Exploratory Data Analysis
