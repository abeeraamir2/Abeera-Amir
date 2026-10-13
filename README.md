# NAVTTC Artificial Intelligence & Machine Learning (Weeks 1 - 5)

[![Python Version](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-blue?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

This repository contains all coursework, exercises, practical implementations, and assignments for the **NAVTTC Artificial Intelligence & Machine Learning** program.

---

## 📂 Repository Structure

```
Week 1-5 NAVTTC Tasks/
├── .gitignore                     # Git ignore rules for Python, Jupyter & IDEs
├── requirements.txt               # Python package dependencies
├── environment.yml                # Conda environment definition
├── README.md                      # Main repository documentation
│
├── Week-01/                       # Week 1: Environment, Linux & Python Basics (Tasks 1 - 25)
│   └── tasks/                     # Python scripts (Tasks 3 - 25)
│
├── Week-02/                       # Week 2: Functions, Exceptions & Stats (Tasks 20, 26, 27, 49, 50)
│   └── tasks/                     # Python scripts
│
├── Week-03-04/                    # Week 3 & 4: NumPy & Pandas Data Stack (Tasks 28 - 48)
│   ├── data/                      # Sample dataset (health_data.csv)
│   └── tasks/                     # NumPy (28-40) & Pandas (41-48) scripts
│
└── Week-05/                       # Week 5: Machine Learning (Tasks 51 & 52)
    └── tasks/                     # Scikit-Learn implementations (Tasks 51 & 52)
```

---

## 🌟 Week 1 Tasks Summary (Tasks 1 - 25)

| Task No. | Task Title | Details |
|:---:|:---|:---|
| **1** | **Installation & Setup** | Anaconda3, PyTorch, TensorFlow 2.0, VS Code, and PyCharm installation guides and verification script. |
| **2** | **Linux Commands** | Detailed reference & hands-on examples for 25+ essential shell commands (`pwd`, `ls`, `grep`, `chmod`, `sudo`, `dpkg`, etc.). |
| **3** | **Python Addition (Predefined)** | Add two predefined numbers (`1.5 + 6.3`) and output formatted sum. |
| **4** | **Python Addition (User Input)** | User input handling, float parsing, and arithmetic addition. |
| **5** | **Square Root (Real Numbers)** | Square root calculation using `** 0.5` and formatted string output. |
| **6** | **Square Root (Complex Numbers)** | Complex math calculation using standard `cmath` module. |
| **7** | **Celsius to Fahrenheit** | Temperature conversion formula $F = (C \times 1.8) + 32$. |
| **8** | **Area of Triangle** | Heron's formula with Triangle Inequality Theorem validation. |
| **9** | **Quadratic Equation Solver** | Roots of $ax^2 + bx + c = 0$ handling both real and complex discriminants. |
| **10** | **Kilometers to Miles** | Unit conversion with factor $0.621371$. |
| **11** | **Conditional Control Flow** | Indentation and branching demonstration with `if` condition. |
| **12** | **If-Else Statement** | Binary branch execution (`if ... else`). |
| **13** | **Nested If Statements** | Multi-level conditional evaluations. |
| **14** | **If-Elif-Else Ladder** | Multi-way condition branching. |
| **15** | **For Loops in Python** | Sequence iteration, range manipulation, and loop-else blocks. |
| **16** | **While Loops in Python** | Counter loops, factorials, digit reversal, and while-else blocks. |
| **17** | **Break Statement** | Premature loop termination and bypassing loop-else blocks. |
| **18** | **Continue Statement** | Iteration skipping (filtering even numbers, vowels, etc.). |
| **19** | **Looping Techniques** | Pythonic iteration: `enumerate()`, `zip()`, `.items()`, `sorted()`, `reversed()`. |
| **21** | **List Data Type** | Creation, slicing, append/extend/insert, pop/remove, sorting & comprehension. |
| **22** | **Tuple Data Type** | Creation, immutability, packing/unpacking, indexing, methods. |
| **23** | **String Data Type** | Slicing, immutability, manipulation methods, f-strings & formatting. |
| **24** | **Set Data Type** | Deduplication, add/update, discard/remove, union, intersection, diff. |
| **25** | **Dictionary Data Type** | Key-value pairs, safe .get(), pop/popitem, methods & dictionary comprehension. |

---

## 🌟 Week 2 Tasks Summary (Functions, Exceptions & Stats)

| Task No. | Task Title | Details |
|:---:|:---|:---|
| **20** | **User-Defined Functions** | Default/keyword arguments, multiple return values, `*args`, `**kwargs`, and lambda expressions. |
| **26** | **Exception Handling** | `try-except-else-finally` lifecycle, handling `ZeroDivisionError`, `ValueError`, `IndexError`. |
| **27** | **User-Defined Exceptions** | Custom exceptions inheriting from `Exception` with domain validation examples. |
| **49** | **Stats: Mean, Median, Mode** | Central tendency metrics using NumPy (`np.mean`, `np.median`) and SciPy (`stats.mode`). |
| **50** | **Stats: Standard Deviation & Variance** | Data dispersion metrics with `np.std()`, `np.var()`, and manual calculation steps. |

---

## 🌟 Week 3 & 4 Tasks Summary (NumPy & Pandas Data Stack - Tasks 28 - 48)

| Task No. | Library | Task Title | Details |
|:---:|:---:|:---|:---|
| **28** | NumPy | **Creating NumPy Arrays** | 0-D to 3-D arrays, inspecting `ndim`, and 5-D arrays with `ndmin`. |
| **29** | NumPy | **NumPy Array Indexing** | Accessing elements across 1-D, 2-D, 3-D, and negative indexing. |
| **30** | NumPy | **NumPy Array Slicing** | 1-D step slicing, negative slices, and 2-D row/column sub-matrices. |
| **31** | NumPy | **Data Types & Casting** | Inspecting `dtype`, specifying types (`'i4'`, `'S'`), and casting via `astype()`. |
| **32** | NumPy | **Copy vs View** | Data ownership rules, memory sharing in views, and `.base` attribute checks. |
| **33** | NumPy | **Array Shape** | Understanding dimensions and tuples returned by `.shape`. |
| **34** | NumPy | **Array Reshaping** | Reshaping 1-D to 2-D/3-D, unknown dimension (`-1`), and array flattening. |
| **35** | NumPy | **Array Iterating** | Standard nested loops, `np.nditer()`, and `np.ndenumerate()`. |
| **36** | NumPy | **Matrix Joining** | `concatenate` along axis 0/1, `stack`, `hstack`, `vstack`, and `dstack`. |
| **37** | NumPy | **Array Splitting** | Dividing arrays into N parts via `np.array_split()`, `np.hsplit()`, `np.vsplit()`. |
| **38** | NumPy | **Array Searching** | Conditional search with `np.where()` and binary search with `np.searchsorted()`. |
| **39** | NumPy | **Array Sorting** | Sorting numbers, alphabetical strings, booleans, and 2-D matrices. |
| **40** | NumPy | **Random Techniques** | Random numbers, arrays, weighted choices, permutations, and seeds. |
| **41** | Pandas | **Pandas Basics** | Tabular dataset creation from dictionaries, dimensions, rows, and columns. |
| **42** | Pandas | **Getting Started** | Installation check, checking version via `pd.__version__`, basic validation. |
| **43** | Pandas | **Series Data** | 1-D labeled arrays, custom index labels, and dictionary-to-Series conversion. |
| **44** | Pandas | **DataFrames** | 2-D tabular data, selecting rows with `.loc[]`, and named row indexes. |
| **45** | Pandas | **Open CSV Files** | Reading CSV files with `pd.read_csv()`, `to_string()`, and `max_rows`. |
| **46** | Pandas | **Data Analyzing** | Data exploration using `.head()`, `.tail()`, `.info()`, and `.describe()`. |
| **47** | Pandas | **Data Cleaning** | Detecting nulls (`isna()`), dropping rows (`dropna()`), imputing medians (`fillna()`), and removing duplicates (`drop_duplicates()`). |
| **48** | Pandas | **Data Correlation** | Calculating Pearson correlation matrix with `.corr()` and relationship analysis. |

---

## 🌟 Week 5 Tasks Summary (Machine Learning with Scikit-Learn)

| Task No. | Task Title | Details |
|:---:|:---|:---|
| **51** | **Linear Regression** | Simple & Multiple Linear Regression, model fitting, parameter estimation (slopes, intercept), and evaluation metrics ($R^2$, MAE, MSE, RMSE). |
| **52** | **Logistic Regression** | Multi-class classification on the MNIST Handwritten Digits dataset (1,797 samples, 8x8 pixels), confusion matrix, and classification report. |

---

## ⚡ Quick Start

### 1. Set Up Environment
Using **Pip**:
```bash
pip install -r requirements.txt
```

Or using **Conda**:
```bash
conda env create -f environment.yml
conda activate navttc-aiml
```

### 2. Run Individual Tasks
```bash
# Example: Run Week 1 Task 3 (Addition)
python Week-01/tasks/task_03_add_two_numbers.py

# Example: Run Week 2 Task 50 (Standard Deviation)
python Week-02/tasks/task_50_standard_deviation.py

# Example: Run Week 3 & 4 Task 28 (NumPy Arrays)
python Week-03-04/tasks/task_28_numpy_create_arrays.py

# Example: Run Week 5 Task 51 (Linear Regression)
python Week-05/tasks/task_51_linear_regression.py
```

---

## 📤 Publishing to GitHub

```bash
# 1. Initialize git repository
git init

# 2. Stage all files
git add .

# 3. Create your commit
git commit -m "Complete NAVTTC Week 1-5 AI/ML tasks and exercises"

# 4. Rename branch to main
git branch -M main

# 5. Link your remote repository
git remote add origin https://github.com/<your-username>/<your-repo-name>.git

# 6. Push to GitHub
git push -u origin main
```
