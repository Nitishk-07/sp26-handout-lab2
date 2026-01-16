from typing import Self

"""
Please implement each of the methods in Vector3D.
There are comments describing each method, but you will need to write documentation.
"""

class Vector3D:
    def __init__(self, x: float, y: float, z: float):
        pass

    def __str__(self) -> str:
        # Should return a string of the form "(x, y, z)"
        # Each number should be rounded to two decimal places
        pass

    def get_magnitude(self) -> float:
        pass

    def normalize(self) -> Self:
        # Return a normalized (magnitude 1) copy of this Vector3D.
        # To do that, divide each component by the magnitude of the vector.
        # Raise a ValueError if the magnitude is zero.
        pass

    def add(self, other: Self) -> Self:
        # Return the sum of this vector and other
        # Do this without changing either of the two original vectors
        pass

    def multiply(self, constant: float) -> Self:
        # Return a copy of this vector, multiplied by the constant
        pass

    def dot_product(self, other: Self) -> float:
        # Return the dot product of this vector and the other vector
        pass
    
    def cross_product(self, other: Self) -> float:
        # Return the cross product of this vector and the other vector
        pass