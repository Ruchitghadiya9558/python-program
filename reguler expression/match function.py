import re

name = input("enter the name:")
patt = "^[a-zA-Z]{2,10}$"

result = re.match(patt,name)
print(result)

if result is None:
    print("Invalid name.... try again")
else:
    print("name is valid")


