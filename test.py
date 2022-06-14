import re
str = "madam i'm adam"
newstr = re.sub(r'[^\w\s]','', str)

print(newstr)