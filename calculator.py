"""
====================================================
 Project:   Command-Line Calculator
 File:      calculator.py
 Author:    Joon Keat Lim
 Created:   2025-09-15
 Version:   1.0
 License:   MIT
====================================================
 Description:
 v1.0:  A simple command-line calculator that supports 
        +, -, *, /, parentheses, power (**), and sqrt().
====================================================
"""

import math

#Update in Latest Version
version = "1.0"

def calculator():
    """
    Run a simple command-line calculator.
    Supports +, -, *, /, **, parentheses, and math functions.
    """
    
    #Print Some Calculator Information To User
    line_notation = "--------------------------------------------------------"
    print(f"\n{line_notation}")
    print(f"Command-Line Calculator v{version} (MIT License)")
    print("Supported operations: +, -, *, /, parentheses, power (**), and sqrt().\n")
    print("Good Day! Thanks for choosing our calculator!")
    print("Enter 'q' to quit the calculator")

    #Calculator Main Functions
    while True:
        expression = input("\nPlease enter your equations:\n\t")
        expression = expression.strip()

        if expression.lower() == 'q':
            print("Quit Calculator! See you next time!\n")
            print(f"\n{line_notation}")
            break
        try:
            result = eval(expression, {"__builtins__": None}, 
                          {"sqrt": math.sqrt, "pow": pow})
            print(f"Your results:\n\t{expression} = {result}")
        except Exception:
            print("Illegal Expression!!! Please try again!\n")


if __name__ == "__main__":
    calculator()
