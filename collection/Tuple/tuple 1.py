mytuple =(10,20,30,40,50,60,"b","add")

print(mytuple[2:5])
print(mytuple[3:8])

print(mytuple[1])
print(mytuple[5])

print(mytuple[-2])
print(mytuple[-4])

if "add" in mytuple:
    print("yes")
else:
    print("no")
print(mytuple)
del mytuple[20]
print(mytuple)
