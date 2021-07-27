# 3 number maximum number

def maximum(a,b,c):
    if (a>b) and (a>c):
        print("A is maximum")
    elif (b>c) and (b>a):
        print("B is maximum")
    elif (c>b) and (c>b):
        print("C is maximum")
num1=int (input("enter the number:"))
num2=int (input("enter the number again:"))
num3=int (input("enter the number:"))
maximum(num1,num2,num3)