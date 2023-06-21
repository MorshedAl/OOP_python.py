
class calculator:
 def product(self,*nums):
  pro=1
  print(nums)
  for x in nums:
   pro=pro*x
  print('product is ',pro)

#================

cal=calculator()
cal.product(4)
cal.product(4,8)
cal.product(4,8,10)

   