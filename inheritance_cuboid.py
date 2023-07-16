#inheritance
# ractangle->cuboid 


class rectangle:
 def __init__(self,l,b):
    self.length=l
    self.breadth=b

 def area(self):
    return self.length*self.breadth

 def perimeter(self):
    return 2*(self.length*self.breadth)

class cuboid(rectangle):
 def __init__(self,l,b,h):
    super().__init__(l,b)
    self.height=h
    
    
 def volume(self):
  return self.length*self.breadth*self.height 


#==================


c1=cuboid(10,5,2)
print(c1.volume())

print('')

c2=cuboid(10,5,3)
print(c2.volume())






