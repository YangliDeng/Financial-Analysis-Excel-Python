# Financial Comparison & Analysis Tool

## Project Overview

This Python project analyzes financial data from **two or more companies** provided as Excel files. It generates **comparative graphs** and a **text-based summary report** to determine:

* Which company is **most profitable**
* Which company is **most concerning**

The analysis is fully automated, reproducible, and based on clearly defined financial metrics.

---

## Team Members & Responsibilities

The project is divided into **three independent modules**, with each team member responsible for one file.

### 👤 Person 1 — Yangli Deng (`data_loader.py`)

**Role:** Data Loading & Validation

**Responsibilities:**

* Read all Excel (`.xlsx`) files from a folder
* Validate that all files follow the same structure
* Ensure required columns exist:

  * `Year`
  * `Revenue`
  * `Expenses`
  * `Net Profit`
  * `Assets`
  * `Liabilities`

* Handle missing or invalid data gracefully
* Extract company name from file name

**Output:**

* A dictionary mapping company names to cleaned pandas DataFrames

---

### 👤 Person 2 — Sarah (`analysis.py`)

**Role:** Financial Analysis & Decision Logic

**Responsibilities:**

* Calculate financial metrics:

  * Average Profit Margin
  * Profit Volatility (standard deviation of Net Profit)
* Compare companies based on calculated metrics
* Determine:

  * **Most Profitable Company**
  * **Most Concerning Company**
* Prepare structured analysis results for reporting

**Notes:**

* This module does **not** handle file I/O or graph generation

---

### 👤 Person 3 — Kyryl (`reporting.py`)

**Role:** Visualization & Reporting

**Responsibilities:**

* Generate and save graphs (`.png`):

  1. Revenue vs Year (Line Chart)
  2. Net Profit vs Year (Line Chart)
  3. Average Profit Margin (Bar Chart)
  4. Profit Volatility (Bar Chart)
* Generate a text summary report (`summary_report.txt`)
* Include the **analysis run date** in the report

**Notes:**

* Uses results produced by `analysis.py`
* Does not perform financial calculations

---

## Project Structure

```text
project/
│
├── data_loader.py      # Yangli
├── analysis.py         # Sarah
├── reporting.py        # Kyryl
├── main.py             # Coordinator
│
├── data/               # Input Excel files
├── output/
│   ├── graphs/         # Generated PNG graphs
│   └── summary_report.txt
```

---

## Input Data Requirements

* One Excel file per company
* Rows represent **years**
* Columns represent **financial metrics**
* All files must follow the **same structure**

Example:

| Year | Revenue | Expenses | Net Profit | Assets  | Liabilities |
| ---- | ------- | -------- | ---------- | ------- | ----------- |
| 2021 | 1000000 | 700000   | 300000     | 2500000 | 1200000     |

---

## Features

* Multi-company financial comparison
* Automated data validation
* Clear, minimal visualizations
* Objective profitability and risk assessment
* Text-based summary report with timestamp
* Modular design for easy collaboration and maintenance

---

## Output

* 📊 Graphs saved as `.png` files
* 📝 Summary report saved as `summary_report.txt`
* 📅 Analysis date included for traceability

---

## Conclusion

This modular design ensures clear responsibility, easy collaboration, and professional-quality output. The project structure reflects real-world software engineering practices and supports scalable financial analysis.
