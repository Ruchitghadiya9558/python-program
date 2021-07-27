import re

msg = "this is an interesting topic"
patt = "\s"

result = re.split(patt,msg)
print(result)

result = re.split(patt,msg,2)
print(result)