import math
def circle_Stats(radius):
   area=math.pi* radius**2
   circumFrence=2*math.pi*radius
   
   return(area,circumFrence)

a,c=circle_Stats(3)
print("Area",a)
print("Circumfrence",c)

