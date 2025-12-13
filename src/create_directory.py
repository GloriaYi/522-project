# create_directory.py
# Creates a directory, if it does not exist.

import os

def create_directory(directory_path):
    """
    Create a directory if it doesn't exist.

    Parameters
    ----------
    directory_path : str
        Path to the directory to create.

    Returns
    -------
    None

    Examples
    --------
    >>> create_directory("data/raw")
    """
    os.makedirs(directory_path, exist_ok=True)