# addition  and count
def add (n):
    box=0
    for i in range(1,n+1):
        box=box + i
    print("count=",box)
num = int(input("enter the number:"))
add (num)
