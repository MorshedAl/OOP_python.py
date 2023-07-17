#Encapsulation

class student:
 def __init__(self,name,Id):
    self.name=name
    self.__Id=Id #private
 
  
 def update_Id(self,Id):
    if Id>0:
     self.__Id=Id
    else:
      print('Invalid ID')




 def details(self):
  print('Name:',self.name,"ID:",self.__Id)

#=============================
s1=student('Nafis',120)
#s1.Id=140  # private বলে আপডেট করা যায়না
s1.update_Id(140) # method মাধ্যমে আপডেট করা যায়

s1.details()








    