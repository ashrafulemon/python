# 5.18  string modification

#add
#remove
#change

#add
index =2
str1= "hello"
str2= str1[:index] +'e'+ str1[index:]
print(str2)

#remove
str2= str1[:index]+str1[index+1:]
print(str2)

#change
str2=str1[:index]+"e"+str1[index+1:]
print(str2)