# 35: set
num1 = {1,2,3,4,5}
num2 = set([4,5,6,7])
num2.add(8)
num2.remove(6)
print(num2)
print(7 in num2)
print(7 not in num2)

print(num1 | num2)
print(num1 & num2)
print(num1 - num2)