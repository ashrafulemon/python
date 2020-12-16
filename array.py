# array
x = [int(i) for i in input().split()] 
print(x)

# creating an empty list 
lst = [] 
n = int(input("Enter elements : ")) 
for i in range(0, n): 
	ele = int(input()) 
	lst.append(ele) 
print(lst) 

# For list of integers 
lst1 = []   
lst2 = []    
lst1 = [int(i) for i in input("Enter items : ").split()] 
lst2 = [i for i in input("Enter items : ").split()]  
print(lst1) 
print(lst2) 


# number of elements 
n = int(input("Enter number of elements : ")) 
a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]  
print("\nList is - ", a) 