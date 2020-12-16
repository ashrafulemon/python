d = 0
while True:
	try:
		a=int (input())
		b=0
		ord=1
		if d:
			print('')
		d = 1
		if (a % 4 == 0) and (not (a % 100 ==0 ) or (a % 400 == 0)):
			print('This is leap year.')
			b = 1
			ord = 0
		if (a % 15 == 0):
			print('This is huluculu festival year.')
			ord = 0
		if (a % 55 == 0 ) and b:
			print('This is bulukulu festival year.')
		if ord:
 			print('This is an ordinary year.')

	except EOFError:
		break