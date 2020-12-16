#65. meta characters
import re
# .  ^  $
pattern = r"^colo.r$"  # . ar jaigai jekono charecter boste pare
                       # ^ soror ongso match korte hobe
                       # $ shes ongso match korte hobe
if re.match(pattern,"colour"):
	print("match")
else:
	print("not match")
#  *
pattern = r"a*"   #(ab)*  0 or jekono songkhok thakte pare
if re.match(pattern,"colour"):
	print("match")
else:
	print("not match")
# +
pattern = r"a+"   # 1 or jekono songkhok thakte pare
if re.match(pattern,"colour"):
	print("match")
else:
	print("not match")
# ?
pattern = r"red(-)?colour"   # ? ar jaigai - ,1 ba 0 bar thakte parbe
if re.match(pattern,"red-colour"):
	print("match")
else:
	print("not match")
# {}
pattern = r"a{1,3}$"  #a 1 ti thke sorbocho 3 ti thakte parbe 
if re.match(pattern,"colour"):
	print("match")
else:
	print("not match")