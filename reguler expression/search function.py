import re

str = "i love cats pet:dog i love cows pet:cows"
patt = "pet:\w\w\w"

result = re.search(patt,str)
print(result)
print(result.span())
print(result.group())
print(result.string)



