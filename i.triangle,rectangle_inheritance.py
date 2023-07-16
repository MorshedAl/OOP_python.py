
#area of triangle, rectangular 

class shape:
 def __init__(self,base,height):
    self.base=base
    self.height=height
  
 def area(self):
    print("shape class!")

class triangle(shape):
 def area(self):
    area=.5*self.base*self.height
    print("triangle area= ",area)
    
class rectangle(shape):
 def area(self):
    area=self.base*self.height
    print("rectangle area= ",area)



t=triangle(10,20)
t.area()


r=rectangle(10,20)
r.area()












