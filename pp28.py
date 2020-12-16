#49 exception handling 2
def voter (age):
	if age <18 :
		raise ValueError("invalid for voter")
	return "you sre allowed to vote"
try:
	print(voter(20))
	print(voter(17))
except ValueError as err:
	print(err)