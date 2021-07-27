# palindrong number

def palindrong(n):
    box=0
    x=n
    while n > 0:
        rem = n % 10
        box= (box *10) + rem
        n=n//10
    if (box==x):
        print("palindrong number")
    else:
        print("not palindrong number")
num = int (input("enter the number:"))
palindrong(num)