#
class sum:
 def __init__(self,x,y):
  self.x=x+y



# operator overloading 
# or adding two objects 

 def __add__(self,other):
  return self.x+other.x





#=========
s1=sum(5,10)
s2=sum(10,25)

print(s1+s2) #s1.__add__(s2)





