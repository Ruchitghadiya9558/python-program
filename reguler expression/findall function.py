import re

msg = "i love cats pet:dog i love cows pet:cows"
patt = "pet:\w\w\w"

result = re.findall(patt,msg)
print(result)