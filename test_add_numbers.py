#!/usr/bin/env python3
"""
Test cases for the add_numbers module.
"""

from add_numbers import add_numbers


def test_add_positive_integers():
    """Test adding positive integers."""
    assert add_numbers(5, 3) == 8
    assert add_numbers(10, 20) == 30


def test_add_negative_integers():
    """Test adding negative integers."""
    assert add_numbers(-5, -3) == -8
    assert add_numbers(-10, 5) == -5


def test_add_floats():
    """Test adding floating point numbers."""
    assert add_numbers(2.5, 1.5) == 4.0
    assert add_numbers(3.14, 2.86) == 6.0


def test_add_mixed_types():
    """Test adding integers and floats."""
    assert add_numbers(5, 2.5) == 7.5
    assert add_numbers(3.0, 7) == 10.0


def test_add_zero():
    """Test adding with zero."""
    assert add_numbers(0, 5) == 5
    assert add_numbers(5, 0) == 5
    assert add_numbers(0, 0) == 0


def test_invalid_input_types():
    """Test that invalid input types raise TypeError."""
    try:
        add_numbers("5", 3)
        assert False, "Should have raised TypeError"
    except TypeError:
        pass
    
    try:
        add_numbers(5, "3")
        assert False, "Should have raised TypeError"
    except TypeError:
        pass
    
    try:
        add_numbers(None, 5)
        assert False, "Should have raised TypeError"
    except TypeError:
        pass


if __name__ == "__main__":
    # Run basic tests without pytest
    print("Running basic tests...")
    
    # Test cases
    test_cases = [
        (5, 3, 8),
        (-5, -3, -8),
        (2.5, 1.5, 4.0),
        (5, 2.5, 7.5),
        (0, 5, 5),
    ]
    
    for a, b, expected in test_cases:
        result = add_numbers(a, b)
        assert result == expected, f"Expected {expected}, got {result}"
        print(f"✓ {a} + {b} = {result}")
    
    print("All tests passed!")