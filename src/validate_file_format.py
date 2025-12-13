# validate_file_format.py
# Checks if the file has the expected file extension.

def validate_file_format(file_path, expected_file_extension):
    """
    Checks if the file has the expected file extension

    Parameters
    ----------
    file_path : str
        Path to the file
    expected_file_extension : str
        Expected extension for file in `file_path`

    Notes
    -----
    Raises ValueError if file format is invalid

    Examples
    --------
    >>> validate_file_format("data.csv", ",csv")
    """

    if not file_path.endswith(expected_file_extension):
        raise ValueError("Invalid file format.")