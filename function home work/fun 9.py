# multiplication number count

def mul(n):
    box=1
    for i in range(1,n+1):
        box=box * i
    print("count=",box)
num = int (input("enter the number:"))
mul(num)
