#63 regular expressions > re
import re
pattern = r"colour"

#match >> prothom ongso match kore ki na ta dekhe
if re.match(pattern,"colour is a colour"):
	print("match")
else:
	print("not match")

#search >> poro tate kothao match kore ki na
if re.search(pattern,"red is a colour"):
	print("match")
else:
	print("not match")	
#findall
print(re.findall(pattern,"red is a colour,i like colour"))