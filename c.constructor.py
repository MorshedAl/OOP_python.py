
#class(design/blueprint) and object(real বস্তু)

class student:
 roll=" "
 gpa=" "
 subject=""
 
 def __init__(self, roll, gpa, subject):
   self.roll=roll
   self.gpa=gpa
   self.subject=subject

 def display(self):
    print(f'Roll:{self.roll}, GPA:{self.gpa}, subject:{self.subject}')

raju=student(88,3.75,'cse')
raju.display()


arif=student(55,3.50,'Economics')
arif.display()


#calculator
class calculator:
 num1=1
 num2=1

 def __init__(self,num1,num2):
    self.num1=num1
    self.num2=num2

 def addd(self):
  return self.num1+self.num2
 

 def substraction(self):
  return self.num1-self.num2
 
  
 def multiply(self):
   return self.num1*self.num2
    
 def division(self):
  return self.num1/self.num2



calculator=calculator(10,20)

ans=calculator.addd()
print(ans)

ans=calculator.substraction()
print(ans)

ans=calculator.multiply()
print(ans)

ans=calculator.division()
print(ans)



    
