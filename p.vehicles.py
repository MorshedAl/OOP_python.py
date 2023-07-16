#polymorphism
# one name but many action 


def driver(gari):
 gari.drive()


class bus:
 def drive(self):
    print("bus is driving ")

class cycle:
 def drive(self):
    print("cycle is driving ")

class motor:

 def drive(self):
    print("motor is driving ")

#===========

b=bus()
driver(b)

m=motor()
driver(m)


c=cycle()
driver(c)
