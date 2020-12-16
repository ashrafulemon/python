i= 1
while True:
	a=input()
	k=0
	if a=='0':
		break
	if i!=1:
		print()
	b=input()
	print("Instancia {}".format(i))
	i=i+1
	#k=(b.find(a))
	#if k>=0:
	if a in b :
		print("verdadeira")
	else:
		print("falsa")
