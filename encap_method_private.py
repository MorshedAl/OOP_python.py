#Encapsulation

class student:
 def __init__(self,name,Id):
    self.name=name
    self.__Id=Id #private

 def details(self):
  print('Name:',self.name,"ID:",self.__Id)
  self.__abc() #class ভিতরে থেকে call করা যাবে।

 def __abc(self):  # private method
   print('private method executed')

#=============================
s1=student('Nafis',120)

#1.__abc() # access করা যায় না।

s1.details()








    