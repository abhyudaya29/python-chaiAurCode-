import math

def  circle_radius(radius):
    area=math.pi *radius**2
    circumfrence=2*math.pi*radius
    return [round(area,2),round(circumfrence,2)]
area,circumfrence=circle_radius(3)
print(area,circumfrence)
