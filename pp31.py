#52 indroducing methods

class student :
	roll = ""
	gpa  = ""
	def set_value (self,roll,gpa):
		self.roll = roll
		self.gpa = gpa
	def display(self):
		print(f"self\n roll:{self.roll}\n gpa:{self.gpa}")

rahim = student()
rahim.set_value(101,3.45)
rahim.display()

karim = student()
karim.set_value(102,3.99)
karim.display()