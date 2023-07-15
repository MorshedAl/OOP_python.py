
"""
class/static/global variable same জিনিস।

class_method access class_variable
class_name.class_method()


static_method isn’t access any variable,instance_variable or class_variable 
class_name.static_method()

"""

# static method
#claculator

class calculator:

 @staticmethod
 def add(a,b):
  return a+b

 @staticmethod
 def sub(a,b):
  return a-b

 @staticmethod
 def mul(a,b):
  return a*b

 @staticmethod
 def div(a,b):
  return a/b


c=calculator() # optional when static method 

print('add:',calculator.add(5,10))
print('sub:',calculator.sub(5,10))
print('mul:',calculator.mul(5,10))
print('division::',calculator.div(5,10))
















