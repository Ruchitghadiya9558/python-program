# number nu addition

class Abc:
    def add(self,n):
        box=0
        for i in range(1,n+1):
            box = box + i
        print("addition=",box)
num = int (input("enter the number :"))

object = Abc()
object . add(num)
