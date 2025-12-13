# validate_column_names.py
# Checks if the column names are valid

def validate_column_names(data, expected_columns):
    """
    Check if the DataFrame has the correct column names

    Parameters
    ----------
    data : DataFrame
        Pandas DataFrame
    expected_columns : list
        List containing the expected columns

    Notes
    -----
    Raises ValueError if column names do not match

    Examples
    --------
    >>> validate_column_names(df, ['one', 'two'])
    """
    
    actual_columns = data.columns.tolist()
    
    missing_columns = set(expected_columns) - set(actual_columns)
    if missing_columns:
        error_msg = "Missing required columns."
        raise ValueError(error_msg)

    extra_columns = set(actual_columns) - set(expected_columns)
    if extra_columns:
        error_msg = "Unexpected extra columns found."
        raise ValueError(error_msg)