#48 exception handling

try:
	list = [20,0,30]
	result = list[0] / list[1]
	print(result)
	print("done")
except ZeroDivisionError:
	print("dividing by zero  is not possible")
except IndexError:
	print("IndexError")
finally:
	print("successful")
#except(ValueError,ZeroDivisionError):
	#print("you have inocrrect input.")