#operator overloading 

class sum:
 def __init__(self,x,y):
  self.x=x+y


# operator overloading/adding two obj. 

 def __add__(self,other):
  return self.x+other.x


s1=sum(5,10)
s2=sum(10,25)

print(s1+s2) #s1.__add__(s2)

#=====================================
# subtract class
class sub:
 def __init__(self,x):
  self.x=x

# operator overloading/subtracting two obj. 
 def __sub__(self,other):
  return self.x-other.x

s1=sub(20)
s2=sub(10)

print(s1-s2) #s1.__sub__(s2)

#=====================================
# Division  __truedive__ // __floordiv__
class sub:
 def __init__(self,x):
  self.x=x

# operator overloading/subtracting two obj. 
 def __truediv__(self,other):
  return self.x/other.x

s1=sub(20)
s2=sub(10)

print(s1/s2) #s1.__truediv__(s2)

#=====================================
# power
class sub:
 def __init__(self,x):
  self.x=x

# operator overloading/subtracting two obj. 
 def __pow__(self,other):
  return self.x**other.x

s1=sub(20)
s2=sub(10)

print(s1**s2) #s1.__pow__(s2)

#=====================================

# grater than
class sub:
 def __init__(self,x):
  self.x=x

# operator overloading
 def __gt__(self,other):
  if self.x>other.x:
    return True
  else: 
    return False

s1=sub(20)
s2=sub(10)

if(s1>s2): #s1.__gt__(s2)
 print("s1 grater")
else:
 print("s2 grater")


#=====================================
class sub:
 def __init__(self,x):
  self.x=x

# operator overloading
 def __eq__(self,other):
  if self.x==other.x:
    return True
  else: 
    return False


s1=sub(20)
s2=sub(20)

if(s1==s2): #s1.__eq__(s2)
 print("s1 & s2 are equal")
else:
 print("not equal")

