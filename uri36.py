import math

a,b,c=input().split()
a=float(a)
b=float(b)
c=float(c)

D = b*b - 4*a*c

if D < 0 or a == 0:
	print("Impossivel calcular")
else:
	x1= (-b + math.sqrt(D))/(2*a)
	x2= (-b - math.sqrt(D))/(2*a)
	print("R1 = {:.5f}".format(x1))
	print("R1 = {:.5f}".format(x2))