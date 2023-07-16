

class Triangle:
 base=1
 height=1

 # constructor 
 def __init__(self,base,height):
   self.base=base
   self.height=height
 
 #method
 def triangle_area(self):
   area=1/2*(self.base*self.height)
   print('Area=',area)

t1=Triangle(10,20)
t1.triangle_area()


t2=Triangle(50,10)
t2.triangle_area()












