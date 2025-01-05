import math
import time

# Enum-like constants for shape types
CIRCLE = 0
RECTANGLE = 1
TRIANGLE = 2

# Function to calculate area using match-case
def calculate_area_match(shape):
    match shape:
        case (CIRCLE, dimension1, _):
            return math.pi * dimension1 ** 2
        case (RECTANGLE, dimension1, dimension2):
            return dimension1 * dimension2
        case (TRIANGLE, dimension1, dimension2):
            return 0.5 * dimension1 * dimension2
        case _:
            return 0.0

# Test function for match-case
def test_match():
    shapes = [
        (CIRCLE, 10.0, 0.0),
        (RECTANGLE, 5.0, 10.0),
        (TRIANGLE, 6.0, 8.0)
    ]

    total_area = 0.0
    for _ in range(10000000):  # Large number of iterations
        for shape in shapes:
            total_area += calculate_area_match(shape)
    print("Total Area (Match-Case):", total_area)

# Abstract Shape class for polymorphism
class Shape:
    def calculate_area(self):
        raise NotImplementedError

# Circle class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

# Rectangle class
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

# Triangle class
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

# Test function for polymorphism
def test_polymorphism():
    shapes = [
        Circle(10.0),
        Rectangle(5.0, 10.0),
        Triangle(6.0, 8.0)
    ]

    total_area = 0.0
    for _ in range(10000000):  # Large number of iterations
        for shape in shapes:
            total_area += shape.calculate_area()
    print("Total Area (Polymorphism):", total_area)

# Function to calculate area using a dictionary mapping
def calculate_area_mapping(shape):
    shape_type, dimension1, dimension2 = shape
    return shape_mapping[shape_type](dimension1, dimension2)

# Dictionary mapping shape types to their area calculation functions
shape_mapping = {
    CIRCLE: lambda r, _: math.pi * r ** 2,
    RECTANGLE: lambda l, w: l * w,
    TRIANGLE: lambda b, h: 0.5 * b * h
}

# Test function for dictionary mapping
def test_mapping():
    shapes = [
        (CIRCLE, 10.0, 0.0),
        (RECTANGLE, 5.0, 10.0),
        (TRIANGLE, 6.0, 8.0)
    ]

    total_area = 0.0
    for _ in range(10000000):  # Large number of iterations
        for shape in shapes:
            total_area += calculate_area_mapping(shape)
    print("Total Area (Mapping):", total_area)

# Function to measure performance
def measure_perf(test_name, func):
    start = time.time()
    func()
    elapsed = time.time() - start
    print(f"{test_name} Elapsed Time: {elapsed:.6f} seconds")

if __name__ == "__main__":
    print("Testing Match-Case:")
    measure_perf("Match-Case", test_match)

    print("Testing Polymorphism:")
    measure_perf("Polymorphism", test_polymorphism)

    print("Testing Mapping:")
    measure_perf("Mapping", test_mapping)