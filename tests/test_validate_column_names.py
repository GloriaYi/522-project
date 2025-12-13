# test_validate_column_names.py
# Tests for validate_column_names

import pytest
import pandas as pd
from src.validate_column_names import validate_column_names

EXPECTED_COLUMNS = [
    "Age",
    "SystolicBP",
    "DiastolicBP",
    "BS",
    "BodyTemp",
    "HeartRate",
    "RiskLevel"
]

def test_validate_column_names_valid():
    """
    Test for valid column names
    """
    
    df = pd.DataFrame(columns=EXPECTED_COLUMNS)
    validate_column_names(df, EXPECTED_COLUMNS)


def test_validate_column_names_missing():
    """
    Test for missing column names
    """
    
    df = pd.DataFrame(columns=EXPECTED_COLUMNS[:-1])  

    with pytest.raises(ValueError, match="Missing required columns"):
        validate_column_names(df, EXPECTED_COLUMNS)


def test_validate_column_names_extra():
    """
    Test for extra column names
    """
    
    df = pd.DataFrame(columns=EXPECTED_COLUMNS + ["ExtraColumn"])

    with pytest.raises(ValueError, match="Unexpected extra columns found"):
        validate_column_names(df, EXPECTED_COLUMNS)
