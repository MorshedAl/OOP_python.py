#currency convertor 
# accessor+ mutator

class currency_convertor:
 def __init__(self,currency,rate):
    self.currency=currency 
    self.rate=rate
   

 def get_currency(self):
  return self.currency 


 def get_rate(self):
    return self.rate
    
 def set_currency(self,currency):
    self.currency=currency 
    
 def set_rate(self,rate):
    self.rate=rate

 def convert(self,amount):
  return self.currency +" conversion to taka is "+ str(self.rate*amount)


#=========================


cc1=currency_convertor('USD',100)
print(cc1.get_currency())
print(cc1.get_rate())

print(' ')
print(cc1.convert(20))

cc1.set_currency('riyal')
cc1.set_rate(25)

print(cc1.convert(10))



