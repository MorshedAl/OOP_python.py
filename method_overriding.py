
#inheritence
class phone:
 def __init__(self):
    print("i am in phone class.")

class iphone(phone):
  pass

i=iphone()



#method overriding 
class phone:
 def __init__(self):
    print("world! phone class.")

class iphone(phone):
  def __init__(self):
    print("I'm in iphone class.")

i=iphone()


# overriding থেকে বাঁচতে super()
class phone:
 def __init__(self):
    print("world! phone class.")

class iphone(phone):
  def __init__(self):
    super().__init__()
    print("I'm in iphone class.")

i=iphone()


