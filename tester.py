from geo.utils import calculate_circle_properties

if __name__ == "__main__":
    radius = 5  
    c, area = calculate_circle_properties(radius)
    print(f"c = {c}") 
    print(f"area = {area}") 
