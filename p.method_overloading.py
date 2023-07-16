#method overloading 
# achieving polymorphism by overloading 

class arithmetic:

 def sum(self,x,y):
    print(x+y)

#=======
a=arithmetic()
a.sum(5,10)

a.sum(5.5,10.5)

a.sum('hellow ','tania!')




class arith:
 
 def add(self,*nums):
  sum=0
  for num in nums:
   sum=sum+num
  print(sum)

#========


a=arith()
a.add(5,10)
a.add(5,10,5)
a.add(5,10,50)
