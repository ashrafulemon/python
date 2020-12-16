#2.13 print basic format
name= "emon"
s_id= 122
mrk=88.899990
#emon 122 88.89999
print(name,s_id,mrk)
print(name, end=" ")
print(s_id,end=" ")
print(mrk)
print(name,s_id,mrk, sep="-")
#emon 122 88.89
print("{} {} {}".format(name, s_id, mrk))
print("{:s} {:d} {:.2f}".format(name, s_id, mrk))