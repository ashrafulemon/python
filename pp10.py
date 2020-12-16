#31 list as input

n=input("Enter your number list : ")
list =n.split()
sum=0
for x in list:
	sum=sum+int(x)
print(sum)