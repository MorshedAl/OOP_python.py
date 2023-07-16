#attribute overriding 

class animal:
 def __init__(self,name):
  self.name=name
  self.color='white'
 
 def walk(self):
  print(self.color,self.name, 'is walking')

class dog(animal):
  def __init__(self,name,color):
    super().__init__(name)
    self.color=color
   
  def eat(self):
    print(self.color, self.name, 'is eating')
    
#===============
d=dog('rover',"red")

d.eat()
d.walk()



