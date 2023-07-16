#inheritance
# polygon-> triangle 

import math

class polygon:
 def __init__(self,ns,*sides):
   self.ns=ns
   self.sides=sides[0:ns]


class triangle(polygon):
 def __init__(self,ns,*sides):
    super().__init__(ns,*sides)
    
 def area(self):
    a,b,c=self.sides
    s=(a+b+c)/2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))


#=====================

t1=triangle(3,5,4,3)
print(t1.area())

t2=triangle(3,6,10,15,30,7) # triangle condition a+b>c
print(t2.area())






    
