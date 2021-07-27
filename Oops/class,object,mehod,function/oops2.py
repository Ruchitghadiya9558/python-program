class Xyz:

    def add(self,a,b):
        sum = a + b
        print("addition =",sum)


num1=int(input("enter the number:"))
num2=int(input("enter the number again:"))

object = Xyz()
object.add(num1,num2)
