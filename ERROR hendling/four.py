n = int (input("enter the number:"))
try:
    if n<=0:
        raise ValueError('number is either zero or negative')
    else:
        print(n)
except ValueError as e:
    print(e)