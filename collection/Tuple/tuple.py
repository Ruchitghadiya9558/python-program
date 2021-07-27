
mytuple=(10,20,30,"a","hello","raj")

print(mytuple)

for i in mytuple:
    print(i)

total = len(mytuple)
print(total)

x = list(mytuple)
print(x)
x[2]="ruchit"
mytuple=tuple(x)
print(mytuple)
