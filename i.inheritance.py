# inheritance:একটা class এর attribute গুলোকে
# অন্য class এ ব্যবহার করা/code reuse করা।

#parent class/Super/base class
class phone:
 def call(self):
  print(" i calling u, dear!")
 
 def sms(self):
  print("i will message u!")


#child/sub/derived class
class iphone(phone):
# def call(self):
#  print(" i calling u, dear!")
 
# def sms(self):
#  print("i will message u!")
 
 def price(self):
    print(120000)

obj=phone()
obj.call()


iphone=iphone()
iphone.call()
iphone.sms()
iphone.price()
