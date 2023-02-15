"""
Roman Numeral Converter

This program takes a decimal number between 1 and 3999 from the user and
converts it to its equivalent Roman numeral.

Author: Kris Armstrong
Date: 02/15/2023
License: MIT

PEP 8 Compliance:
- 4 spaces per indentation level
- Maximum line length of 79 characters
"""

def decimal_to_roman(decimal):
    """
    Convert a decimal number to its equivalent Roman numeral.

    Args:
        decimal (int): The decimal number to convert.

    Returns:
        str: The equivalent Roman numeral.
    """
    # Define the mapping of Roman numeral symbols and their decimal values
    roman_numerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    # Initialize an empty string to build the Roman numeral string
    roman_numeral = ''

    # Iterate through the mapping dictionary to build the Roman numeral string
    for value, symbol in roman_numerals.items():
        while decimal >= value:
            roman_numeral += symbol
            decimal -= value

    return roman_numeral


def validate_input(input_str):
    """
    Validate the user input for a decimal number.

    Args:
        input_str (str): The input string to validate.

    Returns:
        int: The validated decimal number.

    Raises:
        ValueError: If the input is not a valid decimal number.
    """
    try:
        decimal = int(input_str)
        if not (0 < decimal < 4000):
            raise ValueError("Decimal number must be between 1 and 3999.")
    except ValueError:
        raise ValueError("Invalid input. Please enter a valid decimal number.")

    return decimal


def main():
    """
    The primary function of the program.
    """
    # Prompt the user for input
    input_str = input("Enter a decimal number between 1 and 3999: ")

    # Validate the input
    try:
        decimal = validate_input(input_str)
    except ValueError as e:
        print(e)
        return

    # Convert the decimal to its Roman numeral equivalent
    roman_numeral = decimal_to_roman(decimal)

    # Print the Roman numeral equivalent
    print(f"Roman numeral: {roman_numeral}")


if __name__ == '__main__':
    main()
