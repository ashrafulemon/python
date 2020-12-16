#58 types of inheritance
#3type>> hierarchical  multilevel  mulltiple 
# hierarchical >>pp36
#multilevel

class a:
	def dp1(self):
		print("a")
class b(a):
	#dp1
	def dp2(self):
		print('b')
class c(b):
	#dp1
	#dp2
	def dp3(self):
	#ob1.dp1/2 call na korle super use korte hobe
		#super().dp1()
		#super().dp2()
		print('c')

ob1=c()
ob1.dp1()
ob1.dp2()
ob1.dp3()