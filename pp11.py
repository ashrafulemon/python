#31 list input
word=0
letter=0
digit=0
text=input("Give a text : ")
for x in text:
	x=x.lower()
	if x>="a" and x<="z":
		letter=letter+1
	elif x>='0' and x<='9':
		digit=digit+1
	elif x==' ':
		word=word+1
print("letters: ",letter)
print("words  : ",word+1)
print("digits  : ",digit)