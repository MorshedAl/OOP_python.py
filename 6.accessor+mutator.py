# accessor mutator 
# customer

class customer:
 def __init__(self,name,phone):
    self.name=name
    self.phone=phone
  

 def get_name(self):
   return self.name

 def get_phone(self):
   return self.phone

 def set_phone(self,phone):
  self.phone=phone

#================

c1=customer('mr.A',16000)
print(c1.get_name())
print(c1.get_phone())

c1.set_phone(178900)
print(c1.get_phone())

print(' ')

c2=customer('mr.B',19000)
print(c2.get_name())
print(c2.get_phone())

c2.set_phone(178900)
print(c2.get_phone())

