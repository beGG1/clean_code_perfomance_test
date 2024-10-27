import math
from typing import Iterable, Union
from enum import Enum

from utils import decorator


import math
from enum import Enum

# Define an enum for shape types
class ShapeType(Enum):
    SQUARE = 0
    RECTANGLE = 1
    TRIANGLE = 2
    CIRCLE = 3

# Define a structure for shape_union
class ShapeUnion:
    def __init__(self, shape_type, width, height=0):
        self.Type = shape_type
        self.width = width
        self.height = height

# Function to get area using switch-like logic
def get_area_switch(shape):
    result = 0.0
    
    if shape.Type == ShapeType.SQUARE:
        result = shape.width * shape.width
    elif shape.Type == ShapeType.RECTANGLE:
        result = shape.width * shape.height
    elif shape.Type == ShapeType.TRIANGLE:
        result = 0.5 * shape.width * shape.height
    elif shape.Type == ShapeType.CIRCLE:
        result = math.pi * shape.width * shape.width
    
    return result

def total_area(shape_count: int, shapes: Iterable):
    accum = 0.0
    for shape_index in range(shape_count):
        accum += shapes[shape_index].area()
    
    return accum

@decorator
def total_area_vtbl4(shape_count: int, shapes: Iterable):
    accum0 = 0.0
    accum1 = 0.0
    accum2 = 0.0
    accum3 = 0.0
    
    count = shape_count // 4
    index = 0

    while count > 0:
        accum0 += get_area_switch(shapes[index])
        accum1 += get_area_switch(shapes[index + 1])
        accum2 += get_area_switch(shapes[index + 2])
        accum3 += get_area_switch(shapes[index + 3])
        
        count -= 1
    
    result = accum0 + accum1 + accum2 + accum3
    return result

if __name__ == "__main__":
    shapes = [
        ShapeUnion(ShapeType.SQUARE, 2),
        ShapeUnion(ShapeType.RECTANGLE, 3, 4),
        ShapeUnion(ShapeType.TRIANGLE, 3, 4),
        ShapeUnion(ShapeType.CIRCLE, 5)]
    
    result = total_area_vtbl4(1000, shapes)
