#30 guessing game
#import random
from random import randint
for x in range(1,6):
	g_n= int(input("Enter your guessing number: "))
	r_n=randint(1,5)
	if g_n== r_n:
		print(" WOW ,priya loves you so much")
	else:
		print("OHH ,priya miss you")
		print("random number is ",r_n)