import math
class Circle:
    """A class to represent a circle with radius, area, and perimeter properties."""
    def __init__(self, radius):
        """Initializes the circle with a specific radius."""
        self.radius = radius
    def area(self):
        """Computes and returns the area of the circle (π * r²)."""
        return math.pi * (self.radius ** 2)
    def perimeter(self):
        """Computes and returns the perimeter / circumference of the circle (2 * π * r)."""
        return 2 * math.pi * self.radius
if __name__ == "__main__":
    my_circle = Circle(5)
    print(f"Circle Radius: {my_circle.radius}")
    print(f"Area: {my_circle.area():.2f}")
    print(f"Perimeter: {my_circle.perimeter():.2f}")