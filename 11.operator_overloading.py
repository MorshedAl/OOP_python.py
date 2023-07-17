# operator overloading 
# different angle


class Angle:
 def __init__(self,deg):
    self.degree=deg
    

 def __add__(self,other):  # a3=a1+a2 জন্য 
   sum=Angle(self.degree+other.degree) 
   return sum

 def __str__(self): # obj print korle call হয়
   return 'Total angle is '+str(self.degree)



#====================
a1=Angle(30)
a2=Angle(45)
#print(a1)
#print(a2)

a3=a1+a2 # a1.__add__(a2) 

print(a3) 




   