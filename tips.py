
#1 input more

x,y = input("enter number: ").split()
print(x,y)


#2 and conditions

likes=200
comments=50

conditions=[
	likes>100,
	comments>20
]
#if likes>100 and comments>20:
if all(conditions):
	print("emon")


#3 or condition

if any(conditions):
	print("hahaha")


#4 interchange

likes ,comments = comments,likes
print(likes,comments) 


#5 remove doblikat

a= [12,1,2,3,4,5,6,7,4,6,6]
print(a)
a = list(set(a))
print(a)


#6 which number repited most

a= [12,1,2,3,4,5,6,7,4,6,6]
most = max(set(a),key=a.count)
print(most)


#7 

odd =[]
for i in range(11):
	if i%2 ==1:
		odd.append(i**2)
print(odd)
odd1 =[ i**2 for i in range(11) if i%2==1 ]
print(odd1)


#8

def sum (a,b):
	result = 0
	return a+b
res = sum(2,4)
print(res)

def sum(*a):
	result =0
	for i in a:
		result = result+i
	return result
res1 = sum(2,4,23,5)
print(res1)


#9

name = ' emon ashraful priya '[::-1]
print(name)


#10

name1= "madam"
isPlaindrom = name1.find(name1[::-1])==0
print(isPlaindrom)