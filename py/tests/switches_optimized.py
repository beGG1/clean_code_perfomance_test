import math
from typing import Iterable, Union

from utils import decorator


# Define a structure for shape_union
class ShapeUnion:
    def __init__(self, shape_type, width, height=0):
        self.Type = shape_type
        self.width = width
        self.height = height

# Function to get area using switch-like logic
def get_area_if(shape):
    result = 0.0
    
    if shape.Type == 0:
        result = shape.width * shape.width
    elif shape.Type == 1:
        result = shape.width * shape.height
    elif shape.Type == 2:
        result = 0.5 * shape.width * shape.height
    elif shape.Type == 3:
        result = math.pi * shape.width * shape.width
    
    return result

def get_area_match(shape):
    result = 0.0
    
    match shape.Type:
        case 0:
            result = shape.width * shape.width
        case 1:
            result = shape.width * shape.height
        case 2:
            result = 0.5 * shape.width * shape.height
        case 3:
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
        accum0 += get_area_if(shapes[index])
        accum1 += get_area_if(shapes[index + 1])
        accum2 += get_area_if(shapes[index + 2])
        accum3 += get_area_if(shapes[index + 3])
        
        count -= 1
    
    result = accum0 + accum1 + accum2 + accum3
    return result

@decorator
def total_area_vtbl4_match(shape_count: int, shapes: Iterable):
    accum0 = 0.0
    accum1 = 0.0
    accum2 = 0.0
    accum3 = 0.0
    
    count = shape_count // 4
    index = 0

    while count > 0:
        accum0 += get_area_match(shapes[index])
        accum1 += get_area_match(shapes[index + 1])
        accum2 += get_area_match(shapes[index + 2])
        accum3 += get_area_match(shapes[index + 3])
        
        count -= 1
    
    result = accum0 + accum1 + accum2 + accum3
    return result

if __name__ == "__main__":
    shapes = [
        ShapeUnion(0, 2),
        ShapeUnion(1, 3, 4),
        ShapeUnion(2, 3, 4),
        ShapeUnion(3, 5)]
    
    print("____FOR_IF____")
    result = total_area_vtbl4(1000, shapes)
    

    print("____FOR_MATCH____")
    result = total_area_vtbl4_match(1000, shapes)

