
import math

def calculate_circle_properties(radius):
    """Calculate the circumference and area of a circle."""
    c = 2 * math.pi * radius  
    area = math.pi * radius ** 2  
    return c, area
