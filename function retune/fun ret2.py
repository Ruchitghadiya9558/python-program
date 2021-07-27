# 2 number multiplication ane 1 number addition

def mul(a,b):
    sum=a * b
    return (sum)

num1=int(input("enter the number :"))
num2=int(input("enter the number again :"))
ans = mul (num1,num2)
num3=int (input("enter the number:"))

total = ans + num3
print("mul & add=",total)
