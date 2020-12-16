# read a file

file = open("pp25.txt","r+")
print(file.readable())
print(file.writable())
text = file.read()
print(text)
size = len (text)
print(size)
'''text1 = file.readlines()
print(text1)
text2 = file.readlines()[2]
print(text2)
for line in file:
	print(line)'''
file.close()