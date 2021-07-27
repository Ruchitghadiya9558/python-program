# armstrong number
def armstrong (n):
    box=0
    x=n
    while n>0:
        rem = n % 10
        box = box + (rem * rem * rem)
        n=n//10
    if (box==x):
        print("armstrong number")
    else:
        print("not armstrong number")
num = int(input("enter the number:"))
armstrong (num)




