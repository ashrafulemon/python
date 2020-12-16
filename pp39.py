# 59 abstraction
from abc import ABC,abstractmethod
class shape:
 	def __init__(self,dim1,dim2):
 		self.dim1 = dim1
 		self.dim2 = dim2
 	@abstractmethod
 	def area(self):
 		pass  #>>>body na dile pass dite hoi
 		#print("i am area method of shape class")
class triangle(shape):
	def area(self):
		area = 0.5 * self.dim1 * self.dim2
		print("Area of triangle: ",area)
class rectangle(shape):
	def area(self):
		area = self.dim2 * self.dim1
		print("Area of rectangle: ",area)
#s1= shape(10,20)
#s1.area()
t1 = triangle(20,30)
t1.area()
r1 = rectangle(20,30)
r1.area()