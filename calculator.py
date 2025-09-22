"""
====================================================
 Project:   Command-Line Calculator
 File:      calculator.py
 Author:    Joon Keat Lim
 Created:   2025-09-15
 Version:   1.1
 License:   MIT
====================================================
 Description:
 v1.0:  2025-09-15
        A simple command-line calculator that supports 
        +, -, *, /, parentheses, power (**), and sqrt().
 v1.1:  2025-09-22
        Added sin, cos, tan, log, log10, constants (pi, e),
        improved error handling and user interface.
====================================================
"""

import math

#Update in Latest Version
version = "1.1"

safe_math_env = {
    "sqrt":math.sqrt,
    "pow": pow,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "log": math.log,      #Natural Log 
    "log10": math.log10,  #Base 10 Log
    "pi": math.pi,
    "e": math.e
}

def show_help():
    """Provide detailed mathematical functions of the calculator to user"""
    print("\nSupported operations and functions:")
    print(" Basic: +, - , *, /, **, ()")
    print(" Math functions: sqrt(x), pow(x, y), sin(x), cos(x), tan(x), log(x), log10(x)")
    print(" Constants: pi, e")
    print(" Commands: help, exit\n")

def calculator():
    """Run a simple command-line calculator."""
    line_notation = "-" * 56 #As a break line
    print(f"\n{line_notation}")
    print(f"Command-Line Calculator v{version} (MIT License)")
    print("Type 'help' for more instructions, or 'exit' to quit.\n")

    while True:
        try:
            expression = input(">>> ").strip()

            if expression.lower() in ["exit", "quit"]:
                print("Exiting Calculator... Goodbye!\n")
                print(f"\n{line_notation}")
                break
            elif expression.lower() in ["help", "?"]:
                show_help()
                continue

            result = eval(expression, {"__builtins__": None}, safe_math_env)
            print(f"{expression} = {result}\n")
        except Exception as e:
            print(f"[Error] {e}. Please enter a valid expression.")


if __name__ == "__main__":
    calculator()
