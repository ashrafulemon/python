a=input()
a=a.lower()
b=["aeiou"]
c=len(a)
for i in range(0,c):
	if a[i]!='a' and a[i]!='e'and a[i]!='i'and a[i]!='o'and a[i]!='u':
		print(".{}".format(a[i]),end="")
		#print(".",end="")
		#print(a[i],end="")