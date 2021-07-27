# 1 to 4 number addition
def add(n):
    box=0
    for i in range(1,n+1):
        box= box + i
    return (box)
num1=int(input("enter the number:"))
z=add(num1)
num2=int(input("enter the number:"))
total = num2 * z
print(total)