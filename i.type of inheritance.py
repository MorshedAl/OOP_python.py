# example of হায়ারার্কি inheritance 
# একটি class কে অনেকগুলো class inheritance গ্রহণ করে। করে।
 
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


#example of level inheritance 
#A-->B-->C(inheritance)

class A:
 def display1(self):
   print('I\'m in class A')


class B(A):
 # def display1()
 def display2(self):
   print('I\'m in class B')


#one way
"""
class C(B):
 #def display1()
 #def display2()
 def display3(self):
   print('I\'m in class C')

c=C()
c.display1()
c.display2()
c.display3()

"""


#another way
class C(B):
 #def display1()
 #def display2()
 def display3(self):
   super().display1()
   super().display2()
   print('I\'m in class C')

c=C()
c.display3()



#multiple inheritance 
#একাধিক class, একটা class এ inheritance
 
class A:
 def display1(self):
   print('I\'m in class A')

class B:
 def display2(self):
   print('I\'m in class B')

class C(A,B):
 #def display1()
 #def display2()
 def display3(self):
   super().display1()
   super().display2()
   print('I\'m in class C')

c=C()
c.display3()





    
