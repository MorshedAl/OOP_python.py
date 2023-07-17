# method overriding 
# different shape

import math
class shape:
 def __init__(self,name):
    self.name=name
    
 def area(self ):
  print('this is shape class')


class rectangle:
 def __init__(self,l,b):
    self.length=l
    self.breadth=b

 def area(self ): # method overriding 
  return self.length *self.breadth

class circle:

 def __init__(self,r):
    self.radius=r

 def area(self ): #method overriding 
   return math.pi*self.radius*self.radius


#======================
s=shape('heda')
print(s.area())

r=rectangle(10,5)
print(r.area())


c=circle(5)
print(c.area())
   