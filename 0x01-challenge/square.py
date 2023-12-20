#!/usr/bin/python3

class Square:
    """A class representing a square."""

    def __init__(self, side_length):
        """Initialize the Square object.

        Args:
            side_length (int): The length of the square's sides.
        """
        self.side_length = side_length

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.side_length ** 2

    def perimeter(self):
        """Calculate the perimeter of the square.

        Returns:
            int: The perimeter of the square.
        """
        return 4 * self.side_length

    def __str__(self):
        """Return a string representation of the square.

        Returns:
            str: The formatted string representation of the square.
        """
        return f"Square(side_length={self.side_length})"

if __name__ == "__main__":
    s = Square(side_length=12)
    print(s)
    print(s.area())
    print(s.perimeter())
