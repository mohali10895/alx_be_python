# polymorphism_demo.py

import math

class Shape:
    def area(self):
        """Method to be overridden in derived classes."""
        raise NotImplementedError("Subclasses must implement this method.")

class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize the rectangle's length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of the rectangle."""
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        """Initialize the circle's radius."""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * (self.radius ** 2)
