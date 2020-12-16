# 5.20  string search methods 
# count()  find()   index()

s1= "this is a line"

#count
print(s1.count("is"))
print(s1.count("is",4))
print(s1.count("is",4,8))
#find
print(s1.find("is"))
print(s1.find("is",4,8))
print(s1.find("it"))    # na thakle -1 dekhabe

print(s1.index("is"))
#print(s1.index("it"))    error  dekhabe