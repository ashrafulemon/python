import math
x1,y1= input().split()
x2,y2= input().split()
x1=float(x1)
y1=float(y1)
x2=float(x2)
y2=float(y2)
b=(x2-x1);
c=(y2-y1);
d=math.sqrt(b*b + c*c)
print("{:.4f}".format(d))