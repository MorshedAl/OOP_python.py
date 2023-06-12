
#class(design/blueprint) and object(real বস্তু)

class student:
 roll=" "
 gpa=" "
 subject=""
 
 def value_set(self, roll, gpa, subject):
   self.roll=roll
   self.gpa=gpa
   self.subject=subject

 def display(self):
    print(f'Roll:{self.roll}, GPA:{self.gpa}, subject:{self.subject}')

raju=student()
raju.value_set(88,3.5,'economics')
raju.display()


arif=student()
arif.value_set(55,3.75,'economics')
arif.display()


#calculator
class calculator:
 brand="casio"
 num1=1
 num2=1

 def addd(self,num1,num2):
  self.num1=num1
  self.num2=num2
  return num1+num2
 

 def substraction(self,num1,num2):
  self.num1=num1
  self.num2=num2
  return num1-num2
 
  
 def multiply(self,num1,num2):
   self.num1=num1
   self.num2=num2
   return num1*num2
    
 def division(self,num1,num2):
  self.num1=num1
  self.num2=num2
  return num1/num2



calculator=calculator()


ans=calculator.addd(10,20)
print(ans)


ans=calculator.substraction(100,500)
print(ans)


ans=calculator.multiply(10,20)
print(ans)


ans=calculator.division(40,20)
print(ans)



    