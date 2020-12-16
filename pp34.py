#55. inheritance
#supar class /parent class /base class
#sub class /child class/derived class
class phone:               #super class
	def call(self):
		print("call")
	def message(self):
		print("message")
class samsung(phone):      #sub class
	def photo(self):
		print("photo")
s= samsung()
s.message()
s.call()
s.photo()
print(issubclass(samsung,phone))  #subclass jachai korte 