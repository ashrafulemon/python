#24.list 2 >>>
'''.len(), .appand(), .insert(), .remove()
 .sort(), .reverse(), .pop(), .copy(),
 .index(), .count() '''

subject= ["emon","hi","naz","hello"]
print(subject)
print(len(subject))
subject.append("ma")
print(subject)
subject.insert(2,"aaa")
print(subject)
subject.remove("aaa")
print(subject)
subject.sort()
print(subject)
subject.reverse()
print(subject)
subject.pop()
print(subject)
subject2=subject.copy()
print(subject2)
subject.clear()
print(subject)
position1=subject2.index("hi")
print(position1)
count1=subject2.count("hi")
print(count1)