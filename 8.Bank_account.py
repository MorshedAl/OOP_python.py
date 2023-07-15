#Bank account 

class minimum_balance_error(Exception):
 pass

class bank_account:
 account_no=500  #class variable 

 def __init__(self,name,balance=1000):
   if balance<1000:
    raise minimum_balance_error('account cannot be created')
   self.name=name
   self.balance=balance
   self.account_no=bank_account.account_no
   bank_account.account_no +=1



 def deposit(self,amount):
  self.balance +=amount

 def withdraw(self,amount):
   if self.balance-amount<1000:
     raise minimum_balance_error('cannot withdraw')
   self.balance -=amount

 def show_details(self):
  print('person name:',self.name)
  print('account no:',self.account_no)
  print('balance:',self.balance)


#========================

b_acc=bank_account("Abdullah",2000)
b_acc.show_details()
print(' ')

b_acc.deposit(3000)
b_acc.withdraw(1500)
b_acc.show_details()

print(' ')

b_acc2=bank_account("jamshed",7000)
b_acc2.show_details()

