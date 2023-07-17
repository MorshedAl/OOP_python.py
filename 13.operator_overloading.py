# Operator overloading 
# ob3=ob1+ob2 তথা operator দিয়ে অপারেশন করার সময়।
#rational nimber 2/3+5/9=

class rational:
 def __init__(self,p,q):
    self.p=p
    self.q=q


 def __add__(self,other):
   p=self.p*other.q+self.q*other.p
   q=self.q*other.q
  
   return rational(p,q)
  


 def __str__(self):
  return str(self.p) +'/' +str(self.q)

#=========================
r1=rational(2,3)
r2=rational(5,7)

r3=r1+r2

print(r3)





