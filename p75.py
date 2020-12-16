#6.5  leap year

y= 2000

if y%400==0:
	print("leap year")
elif y%100==0:
	print("not leap year")
elif y%4==0:
	print("leap year")
else:
	print("not leap year")


'''
if (y%4==0 and y%100!=0) or y%400==0 :
	print ("leap year")
else
	print("not a leap year")
'''