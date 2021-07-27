# 3 number are max  number

class Abc:
    def max(self,a,b,c):
        if  (a>b) and (a>c):
            print("A is max")
        elif (b>a) and (b>c):
            print("B is max")
        elif (c>a) and (c>b):
            print("C is max")
num  = int (input("enter the number :"))
num1 = int (input("enter the number again :"))
num3 = int (input("enter the number :"))

object = Abc()
object . max(num,num1,num3)