import math
a=float(input("Enter the value of a: "))
b=float(input("Enter the value of b: "))
c=float(input("Enter the value of c: "))
D = b*b - 4*a*c

if D<0 or a==0:
	print("Impossible calcular or Roots are imaginary ")

elif D>0:
	#num_roots = 2
    x= (-b + math.sqrt(D))/(2*a)
    y= (-b - math.sqrt(D))/(2*a)
    print("There are 2 roots: {:f} and {:f}".format (x,y))
elif D==0:
	#num_roots = 1
    x=(-b)/(2 * a)
    print(x," the value is equal")
	
	