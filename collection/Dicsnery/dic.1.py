mydictionary={
"name" : "ruchit",
"city" : "ahmedabad",
"state": "gujrat",
"area" : "nikol"
}

print(mydictionary)

for (i,j) in mydictionary.items():
    print(i,"-------",j)

mydictionary["company"]="praxware"
print(mydictionary)

print(mydictionary["city"])

mydictionary["area"]="hiravadi"
print(mydictionary)

del mydictionary["name"]
print(mydictionary)
