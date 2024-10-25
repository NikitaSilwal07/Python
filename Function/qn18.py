#18.Write a function calculate_area(shape, dimension) that calculates the area of a shape 
# (circle, square, or rectangle) based on the given dimensions.

import math
def calculate_area(shape, dimension):
    if shape.lower()=='circle':
        radius=dimension
        area=math.pi*radius*radius
    elif shape.lower()=='square':
        side=dimension
        area=dimension**2
    elif shape.lower()=='rectangle':
        length,breadth=dimension
        area=length*breadth
    else:
        area="the shape does not match"
    return area

shape = 'rectangle'
dimension = (5,10)  # Length = 5, Breadth = 10

print(f"The area of a {shape} is", calculate_area(shape, dimension))

    
