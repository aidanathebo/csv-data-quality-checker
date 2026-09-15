# CSV Data Quality Checker

A command-line Python tool for analyzing CSV files and chacking their data quality. 

The tool analyzes a CSV dataset, displays the results in the terminal, and generates an HTML report.

## Features

- Reports the number of rows and columns
- Reports the number and percentages of rows with missing values
- Detects and reports the number of duplicate rows
- Identifies numeric and text columns
- Detects outliers in numeric columns using a formula
- Reports the row indices and values of the detected outliers
- Presents the data in the terminal and as an HTML report
- Handles missing, empty, invalid, and non-CSV input files
- Includes automated tests with pytest

## Example Output
```
CSV Data Quality Report
=======================

Rows: 11
Columns: 3

Missing values:
  name: 0 (0.0%)
  age: 0 (0.0%)
  score: 1 (9.1%)

Duplicate rows: 2

Column types:
  name: text
  age: numeric
  score: numeric

Outliers:
  age: 1
    row 4: 36
  score: 3
    row 9: 50.0
    row 10: 59.0
    row 12: 500.0
```

## Installation
- Clone the repository
``` bash 
    git clone YOUR-GITHUB-REPOSITORY-URL
    cd csv-data-quality-checker
```
- Create a virtual environment
``` bash
    python -m venv .venv
```
- Activate it on Windows
``` bash
    .venv\Scripts\activate
```
- Install the requirements 
``` bash
    pip install -r requirements.txt
```

## Usage
- Run the checker by providing the path to a CSV file 
```bash
    python main.py data/example.csv
```
- You can analyze another CSV file by replacing the path
``` bash
    python main.py path/to/your/file.csv
```

## Project Structure
``` text
csv-data-quality-checker/
├── data/                  # Example CSV datasets
├── reports/               # Generated HTML reports
├── src/
│   └── csv_checker/
│       ├── analyzer.py    # Analyzing data quality
│       └── report.py      # Creating the terminal and HTML reports
├── tests/
│   └── test_analyzer.py   # Automated tests
├── main.py                # Command-line entry point
├── requirements.txt       # Python dependencies
└── README.md
```

## Testing

The project uses pytest for automated testing. Run all tests with:
pytest

## Technologies

- Python
- pandas
- pytest
- HTML

