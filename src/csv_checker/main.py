from analyzer import load_csv
from report import print_report


def main():
    df = load_csv("data/example.csv")
    print_report(df)


if __name__ == "__main__":
    main()


    