#Abstract

from abc import ABC,abstractmethod


class parent(ABC):
 
 @abstractmethod
 def show(self): #abstract method (without body)
   pass
 
 def display(self): # concrete method,interface হবে যদি, parent class এ সব বডিছাড়া method হয়
   print('I\'m in parent class')


class child(parent):
  def show(self): # প্রত্যেক child class এ method টি must থাকতে হবে।
    print('I\'m here in child method')

class child2(parent):
 def show(self):
   pass

#=================================

#p=parent() #abstract method থাকলে,               
#p.show() #ঐ class এর object তৈরি করা যায় না

c=child()
c.show()
c.display()

print('')
c2=child2()
c2.display()






