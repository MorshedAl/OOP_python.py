"""
class Bank: 
 def __init__(self, balance): 
  self.balance = balance 
  self.min_withdraw = 100 
  self.max_withdraw = 100000 

 def get_balance(self): 
  return self.balance 

 def deposit(self, amount): 
  if amount > 0: 
    self.balance += amount 
    
 def withdraw(self, amount): 
   if amount < self.min_withdraw: 
     print(f'fokira. you can withdraw below {self.min_withdraw}') 
   elif amount > self.max_withdraw: 
    print (f'bank fokir hoye jabe. you can not with more than {self.max_withdraw}') 
   else: 
    self.balance -= amount 
    print(f'Here is your money {amount}') 
    print(f'your balance after withdraw: {self.get_balance()}') 


brac = Bank(15000)
brac.withdraw(25)
brac.withdraw(50000000)
brac.withdraw(1000) 

dbbl = Bank(5000)
dbbl.deposit(2000)
dbbl.deposit(2000)
print(dbbl.get_balance())

"""

#balance,deposit,withdraw 
class bank:
 def __init__(self,balance):
  self.balance=balance
  self.max_balance=50000
  self.min_balance=100

 def get_balance(self):
  return self.balance 

 def deposit(self,amount):
  if amount>0:
    self.balance +=amount
    
 def withdraw(self,amount):
    if amount>self.max_balance:
       print(f'u cannot withdraw more than {self.max_balance}')
    elif amount<self.min_balance:
       print(f'u cannot withdraw less than {self.min_balance}')
    else:
     self.balance -=amount 
     print(f'here is ur {amount}')
     print(f'after withdraw ur balance {self.get_balance()}')




ibl=bank(20000)

ibl.deposit(10000)
ibl.deposit(5000)

ibl.withdraw(50)
ibl.withdraw(60000)

print('now total balance is ',ibl.get_balance())
ibl.withdraw(15000)



