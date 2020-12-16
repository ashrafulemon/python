#36 stack and queue

# stack
book= []
book.append("aa")
book.append("bb")
book.append("cc")
book.pop()
print(book)
book.pop()
print(book)
book.pop()
if not book:
	print("no book here,")

#Queue
from collections import deque
bank= deque(["aa","bb","cc"])
bank.popleft()
print(bank)
bank.popleft()
print(bank)
bank.popleft()
if not bank:
	print("no people here")