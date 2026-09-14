from analyzer import DataQualityAnalyzer

def print_report(analyzer):

    basic_info = analyzer.get_basic_info()
    missing_values = analyzer.get_missing_values()
    duplicate_count = analyzer.get_duplicate_count()
    column_types = analyzer.get_column_types()
    outliers = analyzer.get_outliers()

    print("CSV Data Quality Report")
    print("=======================")

    print(f"\nRows: {basic_info['rows']}")
    print(f"Columns: {basic_info['columns']}")

    print("\nMissing values:")

    for column, values in missing_values.items():
        print(
            f"  {column}: "
            f"{values['count']} "
            f"({values['percentage']:.1f}%)"
        )

    print(f"\nDuplicate rows: {duplicate_count}")

    print("\nColumn types:")

    for column, column_type in column_types.items():
        print(f"  {column}: {column_type}")

    print("\nOutliers:")
    for column, count in outliers.items():
        print(f"  {column}: {count}")