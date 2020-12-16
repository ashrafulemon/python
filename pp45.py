#64 search and replace >>sub

import re
pattern = r"colour"
text1 = "my favourite colour is red colour"
text2 = re.sub(pattern,"color",text1)
print(text2)
text2 = re.sub(pattern,"color",text1,count=1)
print(text2)