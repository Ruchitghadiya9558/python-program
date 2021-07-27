# addition digit number
def add(n):
    box=0
    while n>0:
        rem=n%10
        box=box + rem
        n=int(n/10)
    print("add=",box)
num=int(input("enter the number:"))
add(num)
