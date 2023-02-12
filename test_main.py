"""
Tests for kilograms to pounds sample program
Andrew Bowman
"""

from main import convert_kilograms_to_pounds

def test_when_no_parameters():
    """
    Tests when no parameters are provided to the function
    """
    assert convert_kilograms_to_pounds() == 0

def test_for_1kg():
    """Test that 1kg == 1lb"""
    assert convert_kilograms_to_pounds(1) == 2.2

def test_for_100kg():
    """Test that 1kg == 1lb"""
    assert int(convert_kilograms_to_pounds(100)) == 220