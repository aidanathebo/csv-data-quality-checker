import pandas as pd

import pandas as pd


def load_csv(file_path):
    if not str(file_path).lower().endswith(".csv"):
        raise ValueError("The file must be a CSV file.")

    try:
        df = pd.read_csv(file_path)

    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")

    except pd.errors.EmptyDataError:
        raise ValueError("The CSV file is empty.")

    except pd.errors.ParserError:
        raise ValueError("The CSV file could not be parsed.")

    return df


class DataQualityAnalyzer:
    def __init__(self, dataframe):
        self.df = dataframe

    def get_basic_info(self):
        return {
            "rows": len(self.df),
            "columns": len(self.df.columns),
        }

    def get_missing_values(self):
        missing = self.df.isnull().sum()
        missing_percentage = (missing / len(self.df)) * 100

        result = {}

        for column in self.df.columns:
            result[column] = {
                "count": int(missing[column]),
                "percentage": float(missing_percentage[column]),
            }

        return result

    def get_duplicate_count(self):
        return int(self.df.duplicated().sum())

    def get_column_types(self):
        result = {}

        for column in self.df.columns:
            if pd.api.types.is_numeric_dtype(self.df[column]):
                result[column] = "numeric"
            else:
                result[column] = "text"

        return result

    def get_outliers(self):
        result = {}

        for column in self.df.select_dtypes(include="number").columns:
            q1 = self.df[column].quantile(0.25)
            q3 = self.df[column].quantile(0.75)

            iqr = q3 - q1

            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr

            outliers = self.df[
                (self.df[column] < lower_bound)
                | (self.df[column] > upper_bound)
            ]


            result[column] = {
            "count": len(outliers),
            "rows": outliers.index.tolist(),
            "values": outliers[column].tolist(),
            }

        return result

    