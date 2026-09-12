import pandas as pd


df = pd.read_csv("data/example.csv")

print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\nColumn names:")
for column in df.columns:
    print("-", column)