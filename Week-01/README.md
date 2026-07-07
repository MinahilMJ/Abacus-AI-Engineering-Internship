# Week 01 - AI Engineering Introduction + Python Foundation

This folder contains the work completed during Week 1 of the Abacus AI Engineering Internship.

The focus of this week was to build a strong foundation in Python programming, understand basic AI Engineering concepts, and develop practical skills through coding exercises and a mini automation project.

---

## Topics Covered

### AI Engineering Fundamentals

* AI Engineer role and responsibilities
* AI Engineer vs ML Engineer
* AI product development lifecycle

---

## Python Programming Practice

The coding practice covered:

### String Manipulation

Implemented programs for:

* Reversing strings without using built-in slicing
* Checking palindrome strings
* Counting character frequency
* Finding the first non-repeating character

### Lists & Arrays

Implemented solutions for:

* Finding the second largest number
* Removing duplicate elements
* Merging sorted lists
* Rotating lists by k positions
* Finding missing numbers from sequences

### Dictionaries & Sets

Implemented programs for:

* Word frequency counting
* Grouping words by first letter
* Finding common elements between lists
* Removing duplicate dictionaries

### Functions

Implemented:

* Custom `map()` function
* Custom `filter()` function
* Custom `reduce()` function
* Recursive factorial
* Recursive Fibonacci

### File Handling

Built programs to:

* Read multiple text files
* Count words and sentences
* Extract frequently used words
* Store results in JSON format

### Exception Handling

Developed a calculator application with:

* Invalid input handling
* Division-by-zero prevention
* Error logging
* Custom exceptions

### Object-Oriented Programming (OOP)

Created classes:

* Employee
* Manager
* Developer

Implemented:

* Inheritance
* Method overriding
* `__str__` method

### Python Problem Solving

Solved problems involving:

* Valid Parentheses
* Longest Common Prefix
* Remove Duplicates from Sorted Array
* Finding Duplicate Numbers

### Comprehensions & Generators

Practiced:

* List comprehensions
* Dictionary comprehensions
* Generator expressions
* Generator functions

---

# Mini Automation Task

## AI Document Processing System

A Python-based document processing automation tool was developed.

The program processes text files, extracts useful information, generates statistics, and stores the results in JSON format.

## Features

* Reads multiple `.txt` files from a folder
* Counts words, characters, and sentences
* Extracts top frequent words
* Generates structured JSON reports
* Handles file processing operations

---

## Input Data

The project processes AI-related text documents:

* `ai_intro.txt`
* `python_basics.txt`
* `machine_learning.txt`
* `deep_learning.txt`

---

## Output

The generated JSON report contains:

* Total number of processed documents
* Individual document statistics
* Word count
* Character count
* Sentence count
* Most frequent words

Example structure:

```json
{
  "total_documents": 4,
  "documents": [
    {
      "filename": "ai_intro.txt",
      "word_count": 46,
      "character_count": 334,
      "sentence_count": 3,
      "top_words": [
        "AI",
        "intelligence",
        "machine",
        "applications",
        "learning"
      ]
    }
  ]
}
```

---

## Project Structure

```text
Week-01/
│
├── Project_Week#01_Abacus_Internship.ipynb
├── summaryOfFileHandling.json
│
├── MiniAutomationTask/
│   ├── data/
│   │   ├── ai_intro.txt
│   │   ├── python_basics.txt
│   │   ├── machine_learning.txt
│   │   └── deep_learning.txt
│   │
│   └── outputs/
│       └── summary_report.json
│
└── README.md
```


---

## Requirements

* Python 3.x
* Jupyter Notebook
