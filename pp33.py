#54. exercise

class triangle:
	base=""
	height=""
	def __init__(self,base,height):
		self.base= base
		self.height= height
		self.area=.5*base*height
	def dp(self):
		#area=.5*self.base * self.height
		print(f"area:{self.area}")

t1=triangle(10,20)
t1.dp()

t2=triangle(20,30)
t2.dp()