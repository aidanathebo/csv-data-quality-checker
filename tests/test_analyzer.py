import pandas as pd
import pytest

from src.csv_checker.analyzer import DataQualityAnalyzer


def test_get_basic_info():
    df = pd.DataFrame({
        "name": ["Alice", "Bob", "Charlie"],
        "age": [21, 22, 23],
    })
    analyzer = DataQualityAnalyzer(df)
    result = analyzer.get_basic_info()

    assert result["rows"] == 3
    assert result["columns"] == 2


def test_get_missing_values():
    df = pd.DataFrame({
        "name": ["Alice", "Bob", "Charlie"],
        "age": [21, None, 23],
    })
    analyzer = DataQualityAnalyzer(df)
    result = analyzer.get_missing_values()

    assert result["name"]["count"] == 0
    assert result["age"]["count"] == 1
    assert result["age"]["percentage"] == 33.33333333333333

def test_get_duplicate_count():
    df = pd.DataFrame({
        "name": ["Alice", "Bob", "Bob"],
        "age": [21, 22, 22],
    })
    analyzer = DataQualityAnalyzer(df)
    result = analyzer.get_duplicate_count()

    assert result == 1


def test_get_column_types():
    df = pd.DataFrame({
        "name": ["Alice", "Bob"],
        "age": [21, 22],
    })
    analyzer = DataQualityAnalyzer(df)
    result = analyzer.get_column_types()

    assert result["name"] == "text"
    assert result["age"] == "numeric"


def test_outlier_detection():
    df = pd.DataFrame({
        "value": [10, 11, 12, 13, 100]
    })
    analyzer = DataQualityAnalyzer(df)
    result = analyzer.get_outliers()

    assert result["value"]["count"] == 1
    assert result["value"]["rows"] == [4]
    assert result["value"]["values"] == [100]




