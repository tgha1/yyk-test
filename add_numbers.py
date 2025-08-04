#!/usr/bin/env python3
"""
A Python program for adding two numbers.

This module provides functionality to add two numbers with proper error handling
and multiple interfaces (function, command-line, and interactive).
"""

import sys
from typing import Union


def add_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Add two numbers together.
    
    Args:
        a: First number (int or float)
        b: Second number (int or float)
    
    Returns:
        The sum of a and b
    
    Raises:
        TypeError: If either argument is not a number
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers (int or float)")
    
    return a + b


def get_number_input(prompt: str) -> float:
    """
    Get a number from user input with validation.
    
    Args:
        prompt: The prompt to display to the user
    
    Returns:
        A valid number from user input
    
    Raises:
        KeyboardInterrupt: If user cancels input
    """
    while True:
        try:
            value = input(prompt)
            return float(value)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            raise


def interactive_mode():
    """Run the program in interactive mode."""
    print("=== Number Addition Calculator ===")
    print("Enter two numbers to add them together.")
    print("Press Ctrl+C to exit.\n")
    
    try:
        while True:
            first_number = get_number_input("Enter the first number: ")
            second_number = get_number_input("Enter the second number: ")
            
            result = add_numbers(first_number, second_number)
            
            # Format output nicely for integers vs floats
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            
            print(f"Result: {first_number} + {second_number} = {result}\n")
            
            continue_choice = input("Add more numbers? (y/n): ").lower().strip()
            if continue_choice not in ['y', 'yes']:
                break
                
    except KeyboardInterrupt:
        print("\nGoodbye!")


def main():
    """Main function to handle command-line arguments or run interactive mode."""
    if len(sys.argv) == 3:
        # Command-line mode with two arguments
        try:
            num1 = float(sys.argv[1])
            num2 = float(sys.argv[2])
            result = add_numbers(num1, num2)
            
            # Format output nicely
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            
            print(f"{num1} + {num2} = {result}")
            
        except ValueError:
            print("Error: Both arguments must be valid numbers.")
            print("Usage: python add_numbers.py <number1> <number2>")
            sys.exit(1)
        except TypeError as e:
            print(f"Error: {e}")
            sys.exit(1)
            
    elif len(sys.argv) == 1:
        # Interactive mode
        interactive_mode()
        
    else:
        # Invalid number of arguments
        print("Usage:")
        print("  python add_numbers.py                    # Interactive mode")
        print("  python add_numbers.py <number1> <number2>  # Command-line mode")
        print("\nExamples:")
        print("  python add_numbers.py 5 3")
        print("  python add_numbers.py 2.5 1.7")
        sys.exit(1)


if __name__ == "__main__":
    main()