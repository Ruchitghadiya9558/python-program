import  math
n = int(input("enter the number:"))
try:
    fac = math.factorial(n)
    print(fac)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)
finally:
    print("program is finished.......")