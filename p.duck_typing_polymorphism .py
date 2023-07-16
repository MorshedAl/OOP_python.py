#polymorphism
# one name but many action 

def pet_lover(pet):
 pet.walk()
# if hasattr(pet,'talk'):
 pet.talk()


class duck:

 def walk(self):
    print("duck is walking")

 def talk(self):
   print("duck is talking")

class dog:
 def walk(self):
    print("dog is walking")

 def talk(self):
  print("dog is talking")

#============

d=duck()
pet_lover(d)

print('')

dog=dog()
pet_lover(dog)

