#53  constructor

class student :
	roll = ""
	gpa  = ""
	def __init__(self,roll,gpa):
		self.roll = roll
		self.gpa = gpa
	def display(self):
		print(f"self\n roll:{self.roll}\n gpa:{self.gpa}")

rahim = student(101,3.44)
rahim.display()

karim = student(101,3.98)
karim.display()