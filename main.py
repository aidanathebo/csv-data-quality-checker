import sys
from src.csv_checker.analyzer import DataQualityAnalyzer, load_csv
from src.csv_checker.report import print_report, generate_html_report


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <csv_file>")
        return

    file_path = sys.argv[1]

    try:
        df = load_csv(file_path)
    except FileNotFoundError:
        print(f"Error: file not found: {file_path}")
        return

    analyzer = DataQualityAnalyzer(df)
    print_report(analyzer)
    generate_html_report(analyzer, "reports/report.html")

if __name__ == "__main__":
    main()