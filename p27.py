#3.3 swap interchange value of two variables
a=5
b=6

a,b =b,a
print(a,b)


a=5
b=6
a=a+b
b=a-b
a=a-b
print(a,b)

a=5
b=6
c=a
a=b
b=c
print(a,b)