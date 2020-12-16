import math
a,b,c= input().split()
a=int(a)
b=int(b)
c=int(c)
d=math.ceil(a/c)
e=math.ceil(b/c)
print(d*e)