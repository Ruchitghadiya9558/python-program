class Abc:
    def add(self,a,b,c=None):
        if c is None:
            sum = a + b
            print("addition:",sum)
        else:
            sum = a + b + c
            print("addition:",sum)
object = Abc()
object.add(10,20)
object.add(10,20,30)