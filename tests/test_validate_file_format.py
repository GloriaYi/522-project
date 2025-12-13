# test_validate_file_format.py
# Tests for validate_file_format

import pytest
import pandas as pd
from src.validate_file_format import validate_file_format

def test_validate_file_format_valid():
    """
    Test to validate a valid file format
    """
    
    validate_file_format("data/raw/maternal_health.csv", ".csv")


def test_validate_file_format_invalid():
    """
    Test to validate an invalid file format
    """
    with pytest.raises(ValueError, match="Invalid file format"):
        validate_file_format("data/raw/maternal_health.txt", ".csv")


def test_validate_file_format_no_ext():
    """
    Test to validate a file with no extension
    """
    with pytest.raises(ValueError, match="Invalid file format"):
        validate_file_format("data/raw/maternal_health", ".csv")