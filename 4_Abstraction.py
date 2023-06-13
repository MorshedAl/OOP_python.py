#abstraction 
# একটা মডেল/standard class তৈরি করা, যাতে সবাই ব্যবহার করতে পারে।
# abstract class তখনই হয়,যখন বডি ছাড়া method থাকে।
# abstract method কে অন্যান্য class এ অবশ্যই ব্যবহার করতে হবে।
# abstract class এর object তৈরি করা যায়না।

from abc import ABC,abstractmethod

class shape(ABC):
 def __init__(self,base,height):
    self.base=base
    self.height=height
    
 @abstractmethod
 def area(self):
    pass
    

class triangle(shape):
 print('haha')
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


