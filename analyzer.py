import pandas as pd


def analyze_csv(file_path):
    df = pd.read_csv(file_path)

    print("Rows:", len(df))
    print("Columns:", len(df.columns))

    print("\nColumn names:")
    for column in df.columns:
        print("-", column)

    missing = df.isnull().sum()
    missing_percentage = (missing / len(df)) * 100

    print("\nMissing values:")

    for column in df.columns:
        count = missing[column]
        percentage = missing_percentage[column]

        print(f"  {column}: {count} ({percentage:.1f}%)")


analyze_csv("data/example.csv")