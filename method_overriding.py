#method overriding 

class animal:
 def __init__(self,name):
  self.name=name
  
 
 def walk(self):
  print(self.name,' is walking ')

class dog(animal):
  def __init__(self,name):
    super().__init__(name)
  
   
  def walk(self):  # method overriding 
  # super().walk()
    print(self.name,' is running')
    
    
#===============
d=dog('rover')
d.walk()



