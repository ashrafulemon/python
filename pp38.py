#types of inheritance
# multiple 
class a:
	def dp(self):
		print("a")
class b:
	def dp(self):
		print('b')
class c(b,a):
	pass
	#def dp(self):
	#	print('c')
ob1=c()
ob1.dp()