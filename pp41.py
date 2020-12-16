#61 magic methods
''' __init__   eq ne lt gt le ge
    add sub mul div'''
class bike:
	def __init__(self,name,color):
		self.name= name
		self.color= color
	def __eq__(self,other):
		return self.name==other.name and self.color==other.color
	def __str__(self):   
		return (f"name={self.name},color ={self.color}")
	def display(self):
		print (f"name={self.name},color ={self.color}")
bike1 = bike("haha","blue")
bike2 = bike("haha","blue")
print(str(bike1))
bike1.display()
print(bike1==bike2)