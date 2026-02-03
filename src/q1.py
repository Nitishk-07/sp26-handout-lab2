"""
Please implement the Calculator class below.
Calculator contains comments describing its methods, but you will need 
to write the method signatures and documentation.
All numbers are floats (arguments and returns).
"""

import unittest

class Calculator:
    pass
    # Methods:
    #   add(a, b) returns a + b
    #   subtract(a, b) returns a - b
    #   multiply(a, b) returns a * b
    #   divide(a, b) returns a / b (or raises ZeroDivisionError)

    def add(self, a: float, b: float) -> float:
        """Returns the sum of a and b."""
        return a + b        
    
    def subtract(self, a: float, b: float) -> float:
        """Returns the difference of a and b."""
        return a - b
    
    def multiply(self, a: float, b: float) -> float:
        """Returns the product of a and b."""
        return a * b


    def divide(self, a: float, b: float) -> float:
        """Returns the quotient of a and b. Raises ZeroDivisionError if b is zero."""
        if b == 0:
            raise ZeroDivisionError("division by zero")
        return a / b
    
