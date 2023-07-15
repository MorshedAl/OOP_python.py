#circle
import math

class circle:
 def __init__(self,radius):
  self.radius=radius

 def area(self):
   return math.pi*self.radius*self.radius

 def perimeter(self):
   return 2*math.pi*self.radius

#=================

c=circle(5)
print("area: ",c.area())

print('perimeter:',c.perimeter())
    