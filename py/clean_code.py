import math
from abc import ABC, abstractmethod
from typing import Iterable, Union
from time import perf_counter
from hwcounter import Timer


class ShapeBase(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(ShapeBase):
    def __init__(self, side: Union[float, int]):
        self.side = side

    def area(self):
        return self.side * self.side

class Rectangle(ShapeBase):
    def __init__(self, width: Union[float, int], height: Union[float, int]):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle(ShapeBase):
    def __init__(self, base: Union[float, int], height: Union[float, int]):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Circle(ShapeBase):
    def __init__(self, radius: Union[float, int]):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

def total_area(shape_count: int, shapes: Iterable):
    accum = 0.0
    for shape_index in range(shape_count):
        accum += shapes[shape_index].area()
    
    return accum

def total_area_vtbl4(shape_count: int, shapes: Iterable):
    accum0 = 0.0
    accum1 = 0.0
    accum2 = 0.0
    accum3 = 0.0
    
    count = shape_count // 4
    index = 0

    while count > 0:
        accum0 += shapes[index].area()
        accum1 += shapes[index + 1].area()
        accum2 += shapes[index + 2].area()
        accum3 += shapes[index + 3].area()
        
        count -= 1
    
    result = accum0 + accum1 + accum2 + accum3
    return result

if __name__ == "__main__":
    shapes = [Square(2), Rectangle(3, 4), Triangle(3, 4), Circle(5)]
    
    start = perf_counter()
    result = total_area_vtbl4(1000, shapes)
    stop = perf_counter()
    
    
    print("Result: ", result)
    print("Total time: ", stop-start)
    
    
    with Timer() as t:
        result2 = total_area_vtbl4(1000, shapes)
    
    print("Result: ", result)
    print(f'Elapsed cycles: {t.cycles:,}')
