def abc(c):
	d=1
	for i in range(1,c+1):
		d=d*i
	return d
while True:
	try:
		a,b =input().split()
		a=int(a)
		b=int(b)
		e=abc(a)
		d=abc(b)
		e=int(e+d)
		print(e)
	except EOFError:
		break

