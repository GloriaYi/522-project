# test_create_directory.py
# Tests for create_directory function

import pytest
import os
from pathlib import Path
from src.create_directory import create_directory

def test_create_new_directory(tmp_path):
    """
    Test creating a new directory
    """
    new_dir = tmp_path / "test_dir"
    assert not new_dir.exists()
    
    create_directory(str(new_dir))
    
    assert new_dir.exists()
    assert new_dir.is_dir()

def test_create_nested_directories(tmp_path):
    """
    Test creating nested directories
    """
    nested_dir = tmp_path / "parent" / "child" / "grandchild"
    
    create_directory(str(nested_dir))
    
    assert nested_dir.exists()
    assert nested_dir.is_dir()

def test_directory_already_exists(tmp_path):
    """
    Test that no error occurs when directory already exists
    """
    existing_dir = tmp_path / "existing"
    existing_dir.mkdir()
    
    # Should not raise an exception
    create_directory(str(existing_dir))
    
    assert existing_dir.exists()

def test_create_directory_with_special_characters(tmp_path):
    """
    Test creating directory with special characters in name
    """
    special_dir = tmp_path / "test_dir_2024_v1.0"
    
    create_directory(str(special_dir))
    
    assert special_dir.exists()

def test_create_directory_with_spaces(tmp_path):
    """
    Test creating directory with spaces in the name
    """
    spaced_dir = tmp_path / "my data folder"
    
    create_directory(str(spaced_dir))
    
    assert spaced_dir.exists()
    assert spaced_dir.is_dir()