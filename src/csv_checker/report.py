from analyzer import (
    get_basic_info,
    get_missing_values,
    get_duplicate_count,
    get_column_types,
)


def print_report(df):
    basic_info = get_basic_info(df)
    missing_values = get_missing_values(df)
    duplicate_count = get_duplicate_count(df)
    column_types = get_column_types(df)

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
