
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
    
    for column, info in outliers.items():
        print(f"  {column}: {info['count']}")

        for row, value in zip(info["rows"], info["values"]):
            print(f"    row {row+2}: {value}")


def generate_html_report(analyzer, output_file):
    basic_info = analyzer.get_basic_info()
    missing_values = analyzer.get_missing_values()
    duplicate_count = analyzer.get_duplicate_count()
    column_types = analyzer.get_column_types()
    outliers = analyzer.get_outliers()

    html = """
    <html>
    <head>
        <title>CSV Data Quality Report</title>
    </head>
    <body>
        <h1>CSV Data Quality Report</h1>
    """

    html += f"<p>Rows: {basic_info['rows']}</p>"
    html += f"<p>Columns: {basic_info['columns']}</p>"

    html += "<h2>Missing Values</h2>"
    html += "<ul>"

    for column, info in missing_values.items():
        html += (
            f"<li>{column}: {info['count']} "
            f"({info['percentage']:.1f}%)</li>"
        )

    html += "</ul>"

    html += f"<h2>Duplicate Rows</h2>"
    html += f"<p>{duplicate_count}</p>"

    html += "</body></html>"

    html += "<h2>Column Types</h2>"
    html += "<ul>"

    for column, column_type in column_types.items():
        html += f"<li>{column}: {column_type}</li>"

    html += "</ul>"

    html += "<h2>Outliers</h2>"

    for column, info in outliers.items():
        html += f"<h3>{column}: {info['count']}</h3>"

        if info["count"] > 0:
            html += "<ul>"

            for row, value in zip(info["rows"], info["values"]):
                html += f"<li>Row {row}: {value}</li>"

            html += "</ul>"

    html += "</body></html>"

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(html)