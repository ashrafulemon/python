#56 method overriding

class phone:
	def __init__(self):
		print("i am in phone class")

class samsung(phone):
	#pass
	def __init__(self):
		#super().__init__()
		print("i am in samsung class")

s= samsung()