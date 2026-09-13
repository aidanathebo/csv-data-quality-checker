import pandas as pd


def load_csv(file_path):
    return pd.read_csv(file_path)


def get_basic_info(df):
    return {
        "rows": len(df),
        "columns": len(df.columns),
    }


def get_missing_values(df):
    missing = df.isnull().sum()
    missing_percentage = (missing / len(df)) * 100

    result = {}

    for column in df.columns:
        result[column] = {
            "count": int(missing[column]),
            "percentage": float(missing_percentage[column]),
        }

    return result


def get_duplicate_count(df):
    return int(df.duplicated().sum())


def get_column_type(column):
    if pd.api.types.is_numeric_dtype(column):
        return "numeric"
    else:
        return "text"


def get_column_types(df):
    result = {}

    for column in df.columns:
        result[column] = get_column_type(df[column])

    return result

