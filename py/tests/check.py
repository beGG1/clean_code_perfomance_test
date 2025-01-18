import math
import time

def calculate_area_match(shape):
    match shape[0]:
        case (0):
            return math.pi * shape[1] ** 2
        case (4):
            return shape[1] * shape[2]
        case (3):
            return 0.5 * shape[1] * shape[2]
        case _:
            return 0.0

def test_match():
    shapes = [
        (0, 10.0, 0.0),
        (4, 5.0, 10.0),
        (3, 6.0, 8.0)
    ]

    total_area = 0.0
    for _ in range(1000000):  # Large number of iterations
        for shape in shapes:
            total_area += calculate_area_match(shape)
    print("Total Area (Match-Case):", total_area)

class Shape:
    def calculate_area(self):
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

def test_polymorphism():
    shapes = [
        Circle(10.0),
        Rectangle(5.0, 10.0),
        Triangle(6.0, 8.0)
    ]

    total_area = 0.0
    for _ in range(1000000):  # Large number of iterations
        for shape in shapes:
            total_area += shape.calculate_area()
    print("Total Area (Polymorphism):", total_area)

def main():
    start_time = time.time()
    test_match()
    print("Match-Case Elapsed Time: {:.6f} seconds".format(time.time() - start_time))

    start_time = time.time()
    test_polymorphism()
    print("Polymorphism Elapsed Time: {:.6f} seconds".format(time.time() - start_time))

if __name__ == "__main__":
    main()