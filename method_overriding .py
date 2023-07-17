#method overriding 


class iphone5:
 
 def show(self):
  print('button')


class iphone13(iphone5):
 def show(self): # method overriding 
  print('touched')
  super().show()

#=====================
i5=iphone5()
i5.show()

print('')
i13=iphone13()
i13.show()










