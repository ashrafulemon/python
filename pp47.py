#character class
import re
pattern = r"[aeiou]"
#pattern = r"[A-Z][a-z][0-9]"

if re.match(pattern,"AiaAg0adsfa"):
	print("match")
else:
	print("not match")