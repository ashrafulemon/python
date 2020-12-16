taka= [100, 50, 20, 10, 5, 2 ,1]
a= int(input())
print(a)
for i in range(0,7):
	b=int(a//taka[i])
	print("{} nota(s) de R$ {},00".format(b,taka[i]))
	a=int(a%taka[i])