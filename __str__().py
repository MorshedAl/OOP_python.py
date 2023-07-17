# __str__()


class student:
 def __init__(self,name):
    self.name=name
    print(self) #same location
    
#================
s1=student('rafi')
print(s1)  #same location   
print(s1.__str__()) #same location 

print('')
#**************************************

class student:
 def __init__(self,name):
    self.name=name
    
    
 def __str__(self):# obj print করলে by default এটা কল হয় এবং location return হয়
  return 'abcd'    #override করলে,location return না হয়ে,str আকারে যা লিখবো রিটার্ন হবে।
#================
s1=student('rafi')
print(s1)    



   