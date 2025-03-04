import math

"""area=(4*p*r^3)/3"""

def volumespher(radius):
    V=(4*math.pi*(radius**3))/3
    return V
    
radius=float(input("radius:"))
print(volumespher(radius))