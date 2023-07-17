# polymorphism 
# pet details 

def my_pet(pet):
    pet.info()
    pet.make_sound()

class cat:
 def __init__(self,name,age):
    self.name=name
    self.age=age
    
 def info(self):
    print('cat name:',self.name,'age:',self.age)

  
 def make_sound(self):
    print('sound:mew mew')



class dog:
 def __init__(self,name,age):
    self.name=name
    self.age=age
    
 def info(self):
    print('dog name:',self.name,'age:',self.age)

  
 def make_sound(self):
    print('sound:gew gew')

#=======================

c=cat('tison',3)
my_pet(c)
d=dog('leperd',5)
my_pet(d)
    