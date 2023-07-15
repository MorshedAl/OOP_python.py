# instance & class variable+method

# Employee details 

class employee:
 employee_count=101 #class variable 

 
 def __init__(self,name,designation,salary):
   self.name=name
   self.designation=designation
   self.salary=salary
   self.eid="e"+str(employee.employee_count)
   employee.employee_count +=1
 
 
 def show_details(self):
    print('name:',self.name)
    print('designation:',self.designation)
    print('salary:',self.salary)
    print('e_id:',self.eid)
    
 @classmethod 
 def total_employee(cls):
   return cls.employee_count-101
    
#=================   

e1=employee("rahim","manager",50000)
print(e1.show_details())

print("")
      
e2=employee("tania","assistant",25000)
print(e2.show_details())
print(" ") 

e3=employee("tania","assistant",25000)
print(e3.show_details())
print(" ") 
        
            
print('total employees:',employee.total_employee())  
          