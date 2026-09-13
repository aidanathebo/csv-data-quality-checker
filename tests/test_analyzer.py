import pandas as pd
import pytest

from src.csv_checker.analyzer import (
    get_basic_info,
    get_missing_values,
    get_duplicate_count,
    get_column_types,
)

def test_get_basic_info():
    df = pd.DataFrame({
        "name": ["Alice", "Bob", "Charlie"],
        "age": [21, 22, 23],
    })

    result = get_basic_info(df)

    assert result["rows"] == 3
    assert result["columns"] == 2


def test_get_missing_values():
    df = pd.DataFrame({
        "name": ["Alice", "Bob", "Charlie"],
        "age": [21, None, 23],
    })

    result = get_missing_values(df)

    assert result["name"]["count"] == 0
    assert result["age"]["count"] == 1
    assert result["age"]["percentage"] == 33.33333333333333

def test_get_duplicate_count():
    df = pd.DataFrame({
        "name": ["Alice", "Bob", "Bob"],
        "age": [21, 22, 22],
    })

    result = get_duplicate_count(df)

    assert result == 1


def test_get_column_types():
    df = pd.DataFrame({
        "name": ["Alice", "Bob"],
        "age": [21, 22],
    })

    result = get_column_types(df)

    assert result["name"] == "text"
    assert result["age"] == "numeric"




