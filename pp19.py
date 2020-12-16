#39: xargs and xxargs  >arguments
#xargs
def student(*details):  
	print(details)
	print(details[0])
student(101,"anis")
student(102,"asf",3.99)

def add(*num):
	sum=0
	for x in num:
		sum=sum+x
	print(sum)
add(10,122)
add(2,34,234,13)

#xx args 
def stu(**detail):
	print(detail)
	print(detail["id"])
	print(detail["name"])
stu(id=101,name="Anis")
