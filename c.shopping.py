
# class shopping 
# __init__
# add_to_cart
# checkout 
# remove
# object create   

            
class shopping:

 def __init__(self,buyer):
   self.buyer=buyer
   self.cart=[] 
 
 def add_to_cart(self,item,price,quantity): 
   product={'item':item, 'price':price,'quantity':quantity}     
   self.cart.append(product)     
 
            
 def checkout(self,amount):        
     total=0
     for item in self.cart:
       total+=item['price']* item['quantity']       
     print('total price=',total ) 
            
     if total>amount:
        print(f'give more money {total-amount}')    
     else:
       print(f'here ur product and extra money {amount-total}')       
            
            
 def remove_item(self,item):
   pass             

tanu=shopping('tania')   
tanu.add_to_cart('watch',1500,15)           
tanu.add_to_cart('rice',70,40)            
tanu.add_to_cart('fish',500,3)         
tanu.add_to_cart('gas',1500,2)          

print(tanu.cart)        
tanu.checkout(30000)           
#tanu.checkout(1700)           
print(tanu.cart)          
            
                     
     
