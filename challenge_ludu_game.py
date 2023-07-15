# ludu game app

from random import *

class ludu:

 def __init__(self,side):
   self.side=side
 
 def dice_rolling(self):
    return randint(1,self.side)

#===============================
d1=ludu(6)

print(d1.dice_rolling())











