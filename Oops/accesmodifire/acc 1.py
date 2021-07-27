# privete function
class Abc:

    def hello(self):
        print(" i am hello function ")
        self.__demo()
        self.__python()
    def __demo(self):
        print("i am demo function")
    def __python(self):
        print("i am python devloper ")
        print("it is not python devloper")

object = Abc()
object.hello()

