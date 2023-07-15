
class book:
 def __init__(self,name,author,price):
    self.name=name
    self.author=author
    self.price=price
 
 
 def details(self):
  print('book_name:',self.name)
  print('autor:',self.author)
  print('price:',self.price)


#============

b1=book('compund effect','D.Hardy',150)
b1.details()

print(' ')

b2=book('Eat That Frog','Brian Tracy',80)
b2.details()
 

