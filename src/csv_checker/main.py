from analyzer import DataQualityAnalyzer, load_csv
from report import print_report


def main():
    df = load_csv("data/example.csv")

    analyzer = DataQualityAnalyzer(df)

    print_report(analyzer)


if __name__ == "__main__":
    main()

    