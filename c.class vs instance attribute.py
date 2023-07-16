#class attribute vs instance attribute


class Shop:
 cart = []
# cart is a class attribute
 def __init__(self, buyer): 
  self.buyer = buyer 
 def add_to_cart(self, item): 
  self.cart.append(item) 
mehzbeeeen = Shop('meh jabeeeen')
mehzbeeeen.add_to_cart('shoes')
mehzbeeeen.add_to_cart('phone')
print(mehzbeeeen.cart) 

nisho = Shop('noisho')
nisho.add_to_cart('cap')
nisho.add_to_cart('watch')
print(nisho.cart)




class shop:
 
 #curt=[] #class attribute 
 def __init__(self,buyer):
   self.cart=[] #instance attribute 
   self.buyer=buyer
 
 def add_to_cart(self,item):
  self.cart.append(item)
  

mrX=shop("mr x")
mrX.add_to_cart('show')
mrX.add_to_cart('watch')
mrX.add_to_cart('t-shirt')
print(mrX.cart)



mrY=shop("mr x")
mrY.add_to_cart('বাদাম')
mrY.add_to_cart('পিঁয়াজু')
mrY.add_to_cart('কনডম')
print(mrY.cart)













