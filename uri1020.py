a=int(input())
b1=a//365
a=a%365
b2=a//30
b3=a%30
print("{} ano(s)\n{} mes(es)\n{} dia(s)".format(b1,b2,b3))